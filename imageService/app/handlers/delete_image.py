from imageService.app.services.s3_service import delete_image
from imageService.app.services.dynamo_service import delete_metadata
from imageService.app.utils.response import response

def handler(event, context):
    image_id = event["pathParameters"]["id"]
    delete_image(image_id)
    delete_metadata(image_id)
    return response(204, {})
