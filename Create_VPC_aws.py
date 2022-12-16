#!/usr/bin/env python3


import boto3

#Create a VPC with Boto3
client = boto3.client("EC2")
client.create_vpc(CidrBlock = '10.10.0.0/16')
