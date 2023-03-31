import json
import boto3
from os import environ, chdir, system
from dbt.tests.util import run_dbt


def setup_profile():
    client = boto3.client('secretsmanager')

    secrets = client.get_secret_value(
        SecretId="iap/dev"
    )['SecretString']

    for key, val in json.loads(secrets).items():
        environ[key] = val



def handler(event, context):
    setup_profile()

    chdir("jaffle_shop")

    system("dbt deps")
    system("dbt build")
    system("dbt run")

    print("All good.")
