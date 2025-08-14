import json
import boto3
import base64
import os
from datetime import datetime

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

UPLOAD_BUCKET = os.environ['UPLOAD_BUCKET']
KNOWN_BUCKET = os.environ['KNOWN_BUCKET']

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        image_data = base64.b64decode(body['image_base64'])
        file_name = f"user_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"

        # Upload user image to S3
        s3.put_object(Bucket=UPLOAD_BUCKET, Key=file_name, Body=image_data)

        # Compare uploaded image with known faces
        results = []
        known_faces = s3.list_objects_v2(Bucket=KNOWN_BUCKET).get('Contents', [])
        
        for face in known_faces:
            response = rekognition.compare_faces(
                SourceImage={'S3Object': {'Bucket': KNOWN_BUCKET, 'Name': face['Key']}},
                TargetImage={'S3Object': {'Bucket': UPLOAD_BUCKET, 'Name': file_name}},
                SimilarityThreshold=80
            )
            for match in response['FaceMatches']:
                results.append({
                    'known_face': face['Key'],
                    'similarity': match['Similarity']
                })

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'matches': results})
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
