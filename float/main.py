import json
import boto3
from os import environ, chdir, system


def setup_profile():
    client = boto3.client('secretsmanager')

    profile = client.get_secret_value(
        SecretId="iap/dev"
    )['SecretString']

    for key, val in json.loads(profile).items():
        environ[key] = val


def handler(event, context):
    setup_profile()

    chdir("jaffle_shop")

    system("dbt deps")
    system("dbt build")

    print("All good.")
