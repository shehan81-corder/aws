
# https://docs.aws.amazon.com/boto3/latest/guide/
# https://docs.aws.amazon.com/boto3/latest/guide/examples.html


# python3 -m pip install boto3
import logging
import boto3
from botocore.exceptions import ClientError

# Create Bucket


def create_bucket(bucket_name, region='us-east-1'):
    # Create bucket
    try:
        bucket_config = {}
        s3_client = boto3.client('s3', region_name=region)
        if region != 'us-east-1':
            bucket_config['CreateBucketConfiguration'] = {
                'LocationConstraint': region}

        s3_client.create_bucket(Bucket=bucket_name, **bucket_config)
        print(f"Bucket created successfully: {bucket_name}")

    except ClientError as e:
        logging.error(e)
        return False
    return True


bucket_name = "shehan-bucket-20261113"
region = "ap-southeast-4"
# create_bucket(bucket_name, region)

# list buckets


def list_buckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


list_buckets()
