#!/bin/bash

echo "Deploy S3 bucket via Cloud Formation";

#This is the stack template
STACK_NAME="cfn-s3-resource"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

aws cloudformation deploy \
--stack-name "$STACK_NAME" \
--no-execute-changeset \
--template-file "$SCRIPT_DIR/template.yaml"