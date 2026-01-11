import boto3
from imageService.app.config import ENDPOINT_URL, AWS_REGION, DYNAMO_TABLE

dynamodb = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION,
    endpoint_url=ENDPOINT_URL
)

table = dynamodb.Table(DYNAMO_TABLE)

def save_metadata(item):
    table.put_item(Item=item)

def list_images(filters=None):
    response = table.scan()
    return response["Items"]

def delete_metadata(image_id):
    table.delete_item(Key={"image_id": image_id})
