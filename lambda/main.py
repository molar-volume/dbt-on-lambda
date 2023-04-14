import boto3
import json
import queue
import threading
import dbt.flags as dbt_flags

from os import environ, chdir
from concurrent.futures import ThreadPoolExecutor


def setup_profile():
    client = boto3.client('secretsmanager')

    profile = client.get_secret_value(
        SecretId="iap/dev"
    )['SecretString']

    for key, val in json.loads(profile).items():
        environ[key] = val


# Override multiprocessing ThreadPool with a ThreadPoolExecutor that doesn't use any
# shared memory semaphore locks
class CustomThreadPool:
    def __init__(self, num_threads):
        self.pool = ThreadPoolExecutor(max_workers=num_threads)

    # provide the same interface expected by dbt.task.runnable
    def apply_async(self, func, args, callback):
        def future_callback(fut):
            return callback(fut.result())

        self.pool.submit(func, *args).add_done_callback(future_callback)

    # we would need to actually keep a "closed" attribute lying around and properly check it
    def close(self):
        pass

    # shutdown(wait=True) mimics "join", whereas shutdown(wait=False) mimics "terminate"
    def join(self):
        self.pool.shutdown(wait=True)


import multiprocessing.dummy

multiprocessing.dummy.Pool = CustomThreadPool


# Replace Multiprocessing context with threaded context
# The objects mostly have the same api
class ThreadedContext:
    Process = threading.Thread
    Lock = threading.Lock
    RLock = threading.RLock
    Queue = queue.Queue


def get_threaded_context():
    return ThreadedContext()


# override both just in case :)
dbt_flags._get_context = get_threaded_context
dbt_flags.MP_CONTEXT = ThreadedContext()


def handler(event, context):
    # when imported here, we're pretty sure the monkey-patching above already took place
    # it also made testing easier (as AWS Lambda keeps old imports around on warm starts)
    import dbt.main as dbt_main
    dbt_main.log_manager._file_handler.disabled = True
    dbt_args = ["--no-write-json", "--use-colors", "build"]

    try:
        setup_profile()
        chdir("dbt_project")
        results, succeeded = dbt_main.handle_and_check(dbt_args)
        # main uses sys.exit which doesn't play well with the AWS Lambda handler
    except Exception as e:
        # This is to ease debugging, the exception catching should be rewritten properly
        message = str(e)
        results = None
        succeeded = False
    else:
        message = "OK"

    print(message)
    return {
        'statusCode': 200,
        'body': {
            'message': message,
            'results': str(results),
            'succeeded': succeeded
        }
    }
