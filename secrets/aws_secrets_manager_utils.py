import os
import boto3
import json

from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()
AWS_REGION = os.getenv("AWS_REGION", "us-central-1")


def get_aws_secret(environment, region_name: str = AWS_REGION):
    secret_name = environment

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id=os.getenv("AWS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET"),
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']

    secret_json = json.loads(secret)
    return secret_json
