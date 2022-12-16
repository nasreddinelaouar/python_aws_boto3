#!/usr/bin/env python3

import boto3

client = boto3.client("EC2")
response = client.delete_vpc(VpcId ='vpc-vpcid')
response
