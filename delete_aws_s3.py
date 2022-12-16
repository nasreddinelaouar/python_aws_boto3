#!/usr/bin/env python3


import boto3

resource=boto3.client("S3")

#delete a single object
resource.delete_object(Bucket = 'aws_python_boto3', Key = 'S3_test.jpg')
      
#find all the objects from the bucket
objects = resource.list_objects(Bucket = "aws_python_boto3")["Contents"]
len(objects)

#Iteration
for object in objects:
    response = resource.delete_object(Bucket = 'aws_python_boto3', Key = object["Key"])
print(response)