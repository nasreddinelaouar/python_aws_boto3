#!/usr/bin/env python3

#This is a script to search for the S3 creation date
import boto3

s3_resource = boto3.client("s3")
s3_resource.list_buckets()["Buckets"][0]["Name"]
creation_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
creation_date.strftime("%m%d%y_%H:%M:%s")


for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])
