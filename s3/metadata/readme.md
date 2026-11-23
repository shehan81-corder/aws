# Metadata

Put an object into S3 with metadata

```sh
aws s3api put-object --bucket shehan-test-november26 --key test.txt --body test.txt --metadata Planet=mars
```

List head object

```sh
aws s3api head-object --bucket shehan-test-november26 --key test.txt
```
