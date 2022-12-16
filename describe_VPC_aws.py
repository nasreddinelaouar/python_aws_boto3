#!/usr/bin/env python3

import boto3

client = boto3.client("EC2")

#describe a VPC
x = client.describe_vpcs()
number_of_vpcs = x["VPCs"]
len(number_of_vpcs)

for vpc in number_of_vpcs:
    print(vpc["VPCID"])
    
#describe a single VPC based on the VPC ID
x = client.describe_vpcs(VpcIds = "VPC-ID")


