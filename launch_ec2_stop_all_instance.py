#!/usr/bin/env python3.7

import boto3


ec2 = boto3.resource("ec2", region_name = "us-east-1")
#SubnetId = ''
#VPC_ID = "vpc-0d6117f29e10b2a0b"
#VPC_ID = "vpc-02e710b23b7ad09ef"
#SubnetId = "subnet-06cb91475c7ec0b78"
#SECURITY_GROUP_ID = "sg-09fc1169a36554bc3"

instances = ec2.create_instances(
    ImageId="ami-0b5eea76982371e91",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1
    )
    
print(instances["Instances"][0]["InstanceId"])


"""       
def describe_ec2_instance():
    try:
        print ("Describing EC2 instance")
        ec2 = boto3.client("ec2")
        print(ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)
        
        
        
def stop_ec2_instance():
    try:
        print ("Stop EC2 instance")
        instance_id = describe_ec2_instance()
        ec2 = boto3.client("ec2")
        print(ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)
"""