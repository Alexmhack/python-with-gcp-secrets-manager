import os

from fastapi import FastAPI

from secrets.secret_manager import get_secret

app = FastAPI()
DEBUG = os.getenv("DEBUG", "LEARNING")


@app.get("/")
def version_api():
	secrets = get_secret(DEBUG)
	return {"version": secrets.API_VERSION}
