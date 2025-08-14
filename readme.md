# Facial Recognition Web App using AWS

A serverless web app for real-time face detection & matching using AWS Rekognition, S3, Lambda, and API Gateway.

## 🚀 Features
- Upload image via web browser
- Compare with stored "known faces"
- Return matches with confidence score

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** AWS Lambda (Python)
- **Face Recognition:** AWS Rekognition
- **Storage:** Amazon S3
- **API:** AWS API Gateway

## 📦 Setup Instructions
1. Create S3 buckets:  
   - `facial-recognition-uploads`  
   - `facial-recognition-known-faces`
2. Upload reference images to `known-faces` bucket.
3. Create Lambda function with `lambda_function.py` and attach IAM role with:
   - AmazonS3FullAccess
   - AmazonRekognitionFullAccess
4. Create API Gateway (POST) → Connect to Lambda → Enable CORS.
5. Update `API_URL` in `frontend/index.html`.
6. Host frontend using S3 static hosting or AWS Amplify.

## 📄 License
MIT
