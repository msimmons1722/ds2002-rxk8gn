import boto3
import requests
import sys
import os

def download_file(url, local_filename):
    with open(local_filename, "wb") as file:
        file.write(requests.get(url).content)

def upload_to_s3(local_file, bucket, s3_key):
    boto3.client("s3").upload_file(
        local_file, bucket, s3_key, ExtraArgs={"ACL": "private", "ContentType": "image/gif"}
    )

def generate_presigned_url(bucket, s3_key, expiration):
    return boto3.client("s3").generate_presigned_url(
        "get_object", Params={"Bucket": bucket, "Key": s3_key}, ExpiresIn=int(expiration)
    )

if __name__ == "__main__":
    file_url, bucket_name, expiration_time = sys.argv[1], sys.argv[2], sys.argv[3]
    local_filename = os.path.basename(file_url)

    download_file(file_url, local_filename)
    upload_to_s3(local_filename, bucket_name, local_filename)
    print(generate_presigned_url(bucket_name, local_filename, expiration_time))
