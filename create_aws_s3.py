#!/usr/bin/env python3

#Creation of S3 bucket 

import boto3


AWS_REGION = "us-east-1"

resource = boto3.resource("s3", region_name=AWS_REGION)

bucket_name = "aws_python_boto3"
location = {'LocationConstraint': AWS_REGION}

bucket = resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)

print("S3 bucket has been created")
