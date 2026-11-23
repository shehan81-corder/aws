from aws_cdk import (
    Stack,
    CfnOutput,
    aws_s3 as s3,
)
from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Define a private bucket for this practice stack.
        bucket = s3.Bucket(
            self,
            "PracticeBucket"
        )

        # Display the generated bucket name after deployment.
        CfnOutput(
            self,
            "BucketName",
            value=bucket.bucket_name,
        )
