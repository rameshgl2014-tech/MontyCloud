import uuid
import base64
from imageService.app.services.s3_service import upload_image
from imageService.app.services.dynamo_service import save_metadata
from imageService.app.utils.response import response
from imageService.app.utils.logger import get_logger

logger = get_logger(__name__)

def handler(event, context):
    """
    POST /upload
    Upload image + metadata
    """
    try:
        body = event["body"]

        # Decode Base64 image
        image_bytes = base64.b64decode(body["image"])

        # Generate unique image ID
        image_id = str(uuid.uuid4())

        # Upload to S3
        upload_image(image_id, image_bytes)

        # Save metadata in DynamoDB
        save_metadata({
            "image_id": image_id,
            "user": body["user"],
            "tags": body.get("tags", [])
        })

        return response(201, {
            "message": "Image uploaded successfully",
            "image_id": image_id
        })

    except Exception as e:
        logger.exception("Image Uploading  failed reason : {0} ".format(str(e)))
        return response(500, {"error": "Internal Server Error"})



