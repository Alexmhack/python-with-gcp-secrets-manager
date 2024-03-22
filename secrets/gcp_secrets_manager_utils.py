import os
import json

from google.cloud import secretmanager

GCP_REGION = os.getenv("GCP_REGION", "asia-south1")


def get_gcp_secret(environment, region_name: str = GCP_REGION):
	secret_label = environment

	client = secretmanager.SecretManagerServiceClient()
	gcloud_secret_name = f"projects/295487836532/secrets/{secret_label}/versions/latest"
	payload = client.access_secret_version(name=gcloud_secret_name).payload.data.decode("UTF-8")

	secret_json = json.loads(payload)
	return secret_json
