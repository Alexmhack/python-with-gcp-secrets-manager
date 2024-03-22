import os
from functools import lru_cache

from .utils import AttrDict
from .aws_secrets_manager_utils import get_aws_secret
from .gcp_secrets_manager_utils import get_gcp_secret


@lru_cache
def get_secret(environment):
    SECRET_MANAGER_PROVIDER = os.getenv("SECRET_MANAGER_PROVIDER")
    if SECRET_MANAGER_PROVIDER == "aws":
        secrets = get_aws_secret(environment)
    elif SECRET_MANAGER_PROVIDER == "gcp":
        secrets = get_gcp_secret(environment)
    else:
        raise Exception(f"Unknown SECRET_MANAGER_PROVIDER: {SECRET_MANAGER_PROVIDER} found")

    return AttrDict(secrets)
