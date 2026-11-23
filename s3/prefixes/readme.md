# Object Prefixes

An S3 prefix is the beginning part of an object's key (name), commonly used to organise and filter objects.

my-saas-bucket
    invoices/
        2025/
            jan.pdf
            feb.pdf
        2026/
            jan.pdf
    customers/

For the object invoices/2026/jan.pdf:

- Bucket: my-saas-bucket
- Object key: invoices/2026/jan.pdf
- Prefix: invoices/2026/

Important: S3 uses a flat object structure. These folders are logical, created using prefixes rather than actual directories.


Test This:

## Step 1. Upload files with different prefixes

```sh
echo "January Invoice" > jan.txt
echo "February Invoice" > feb.txt
```

Copy them

```sh
aws s3 cp jan.txt s3://BUCKET_NAME/invoices/2026/jan.txt
aws s3 cp jan.txt s3://BUCKET_NAME/invoices/2026/feb.txt
```

## List objects using a prefix

```sh
 aws s3api list-objects --bucket BUCKET_NAME
 aws s3api list-objects --bucket BUCKET_NAME --prefix "invoices/2027" --query "Contents[].Key"
 aws s3api list-objects --bucket BUCKET_NAME --prefix "invoices/" --delimiter "/"
```