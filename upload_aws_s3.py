#!/usr/bin/env python3
import boto3


#Uploading a single file to S3
resource = boto3.client("S3")
resource.upload_file(
    Filename = "S3_test.png",
    Bucket = "aws_python_boto3",
    Key = "S3_test_diagram.png")
    
    
#Uploading a multiple files to S3
import os
import glob

cwd=os.getcwd()

cwd=cwd+"/upload/"

files=glob.glob(cwd+"*.jpg")

files
 
for file in files:
    resource=boto3.client("s3")
    resource.upload_file(Filename=file, Bucket="aws_python_boto3", Key=file.split("/")[-1])
    
    
