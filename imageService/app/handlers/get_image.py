from imageService.app.services.s3_service import get_image
import base64

def handler(event, context):
    image_id = event["pathParameters"]["id"]
    data = get_image(image_id)

    return {
        "statusCode": 200,
        "body": base64.b64encode(data).decode(),
        "isBase64Encoded": True
    }
