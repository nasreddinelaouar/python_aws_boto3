#!/usr/bin/env python3

import boto3

resource = boto3.client("s3")
objects = resource.list_objects(Bucket="aws_python_boto3")["Contents"]

len(objects)

if len(objects)>0:
    print("objects are existing")

for object in objects:
    print(object["Key"])
    
    