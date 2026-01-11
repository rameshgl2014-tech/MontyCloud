import boto3
from imageService.app.config import ENDPOINT_URL, AWS_REGION, S3_BUCKET

s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    endpoint_url=ENDPOINT_URL
)

def upload_image(key, data):
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=data)

def get_image(key):
    return s3.get_object(Bucket=S3_BUCKET, Key=key)["Body"].read()

def delete_image(key):
    s3.delete_object(Bucket=S3_BUCKET, Key=key)
