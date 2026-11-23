# Checksums

## Checksums are primarily about data integrity, not security or availability

This verifies the integrity of the file in transit to ensure the fie is not corrupted.

AWS uses different algorithms /hashing mechanisms to do this.

Common Algorithms supported by S3
CRS32, CRC32C, SHA1, SHA256, MD5
Ex. Before uploading, the computer generates the checksum from the file., Once uploaded s3 will calculate its own checksum and compare. If the integrity is failed, they reject the upload.

Test This:

## Step 1. Create a test file

echo "Hello AWS S3 Checksum" > test.txt

## Step 2. Calculate its checksum locally

shasum -a 256 test.txt
f1408d7b5f2033304bce8d4b0ba29f25b9606ae6b45299a627e69c6d8d0ef0ae  test.txt
However, S3 returns SHA256 checksums in Base64 format, so let's calculate the same checksum in Base64.

openssl dgst -sha256 -binary test.txt | openssl base64 -A
8UCNe18gMzBLzo1LC6KfJblgaua0UpmmJ+acbY0O8K4=%  

CHECKSUM=$(openssl dgst -sha256 -binary test.txt | openssl base64 -A)
echo "$CHECKSUM"

## Step 3. Upload the file with its checksum

aws s3api put-object \
  --bucket YOUR_BUCKET_NAME \
  --key test.txt \
  --body test.txt \
  --checksum-sha256 "$CHECKSUM"

{
    "ETag": "\"90e1af6e0713dbbd6086bd0c5acd9e61\"",
    "ChecksumSHA256": "8UCNe18gMzBLzo1LC6KfJblgaua0UpmmJ+acbY0O8K4=",
    "ChecksumType": "FULL_OBJECT",
    "ServerSideEncryption": "AES256"
}

## Step 4. Retrieve the checksum from S3

aws s3api head-object \
  --bucket YOUR_BUCKET_NAME \
  --key test.txt \
  --checksum-mode ENABLED

  {
    "AcceptRanges": "bytes",
    "LastModified": "2026-11-20T03:07:37+00:00",
    "ContentLength": 26,
    "ChecksumSHA256": "8UCNe18gMzBLzo1LC6KfJblgaua0UpmmJ+acbY0O8K4=",
    "ChecksumType": "FULL_OBJECT",
    "ETag": "\"90e1af6e0713dbbd6086bd0c5acd9e61\"",
    "ContentType": "binary/octet-stream",
    "ServerSideEncryption": "AES256",
    "Metadata": {}
}

## Step 5. Test a checsum failure

Upload a file with an incorrect checksum

aws s3api put-object --bucket shehan-bucket-20261113 --key testfail.txt --body testfail.txt --checksum-sha256 8UCNe18gMzBLzo1LC6KfJblgaua0UpmmJ+acbY0O8K4=%  
aws: [ERROR]: An error occurred (InvalidRequest) when calling the PutObject operation: Value for x-amz-checksum-sha256 header is invalid.

## What should you remember for AWS SAA?

- Checksum: Verifies data integrity.
- Encryption: Protects data confidentiality.
- Versioning: Helps recover previous versions of objects.
- ETag: Identifies an object version's content, but is not always an MD5 checksum.
- S3 checksum validation: Detects corrupted data during uploads and downloads.

A checksum answers the question, "Did the data arrive intact?" It does not answer, "Is the data secure?"