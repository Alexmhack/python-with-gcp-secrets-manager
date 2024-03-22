# python-with-secrets-manager

This is a very basic FastAPI application that makes use of Secrets Manager Providers like [AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) & [GCP](https://cloud.google.com/security/products/secret-manager).

You can take reference from the code for better understanding, below are listed a few points to be noted for using and managing 
secrets in Secrets Manager Provider.

1. AWS provides us option to add *Other type of secret* which basically allows us to store Key/Value pairs as secrets, this is very 
helpful as we can store lots of key value pairs and make use of them as a dictionary in Python code.
	![AWS - Other type of secret](https://github.com/Alexmhack/python-with-secrets-manager/blob/master/readme_images/aws_secret_type.png)

2. On the other hand, GCP does not allow this option and instead we have a text based input, but we can definitely enter JSON format 
there and store it and later on access this as a dictionary in Python code.
	![GCP - Text type of secret only](https://github.com/Alexmhack/python-with-secrets-manager/blob/master/readme_images/gcp_secret_type.png)

3. We are using `lru_cache` from `itertools` to cache our secrets once they have being retrieved in the Python code, which is a good 
way to fetch secrets very fast after initial loading but the secrets value won't change until the server has been restarted which is 
serving FastAPI app.

4. `AttrDict` -> This is a custom written utility which helps to convert a Python dict to a class object which has access to all the dict keys using `.` notation. For e.g. if a secret is `{"API_VERSION": "14"}` then using `AttrDict` instance we can access it using `attr_dict_instance.API_VERSION  # output -> 14`


## AWS Setup

![AWS - Image showing secret stored in AWS console](https://github.com/Alexmhack/python-with-secrets-manager/blob/master/readme_images/aws_first_image.png)

## GCP Setup

![GCP - Image showing secret stored in GCP console](https://github.com/Alexmhack/python-with-secrets-manager/blob/master/readme_images/gcp_first_image.png)
