# Copy a file to a bucket

```sh
aws s3 cp file.txt s3://shehan-november-26/file.txt
```

Set the storage class

```sh
aws s3 cp file.txt s3://shehan-november-26/file2.txt --storage-class=STANDARD_IA
```

## Cleanup

```sh
aws s3 rm s3://shehan-november-26/file.txt
aws s3 rm s3://shehan-november-26/file2.txt
aws s3 rb s3://shehan-november-26
```