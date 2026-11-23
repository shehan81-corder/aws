from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3
)
from constructs import Construct


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        s3.Bucket(
            self,
            "PracticeBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )
