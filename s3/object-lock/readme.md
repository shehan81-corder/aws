# WORM / Object Lock / Versioning

## Create a bucket with lock mode

```sh
aws s3api create-bucket \
  --bucket shehan-test-lock-november26 \
  --region ap-southeast-4 \
  --create-bucket-configuration LocationConstraint=ap-southeast-4 \
  --object-lock-enabled-for-bucket
```

## Put an object

## Apply a governance retention period

```sh
aws s3api put-object-retention \
  --bucket YOUR_UNIQUE_BUCKET_NAME \
  --key audit.txt \
  --retention 'Mode=GOVERNANCE,RetainUntilDate=2026-11-22T00:00:00Z'
```

## Retrive the new file version

```sh
aws s3api list-object-versions \
  --bucket YOUR_UNIQUE_BUCKET_NAME \
  --prefix audit.txt
```

## Try to delete the specific version

```sh
aws s3api delete-object \
  --bucket YOUR_UNIQUE_BUCKET_NAME \
  --key audit.txt \
  --version-id YOUR_VERSION_ID
```

aws: [ERROR]: An error occurred (AccessDenied) when calling the DeleteObject operation: Access Denied because object protected by object lock.
