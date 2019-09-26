import os
import boto3, botocore

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ["S3_KEY"],
   aws_secret_access_key=os.environ["S3_SECRET"]
)

def upload(file):
	s3.upload_fileobj(
		file,
		os.environ["S3_BUCKET"],
		file.filename,
		ExtraArgs={
			"ACL": 'public-read',
			"ContentType": file.content_type
		}
	)
	return f"https://{os.environ['S3_BUCKET']}.s3.amazonaws.com/" + file.filename