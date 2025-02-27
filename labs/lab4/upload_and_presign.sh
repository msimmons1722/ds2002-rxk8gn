#!

LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3
S3_KEY=$(basename "$LOCAL_FILE")

aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/$S3_KEY" --acl private

PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET_NAME/$S3_KEY" --expires-in "$EXPIRATION")

echo "$PRESIGNED_URL"
