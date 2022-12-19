#!/usr/bin/env python3.7
import boto3

ec2 = boto3.resource("ec2")

instances = ec2.create_instances(
    ImageId="ami-0b5eea76982371e91",
    InstanceType="t2.micro",
    MinCount=3,
    MaxCount=3,
    SubnetId = "subnet-0d4aa9f756b19fcd3",
    TagSpecifications=[
        {
            "ResourceType" : "instance",
            "Tags" : [
                
                {
                   "Key" : "Name",
                   "Value" : "Ops-environment",
                },
                {
                    "Key" : "environment",
                    "Value" : "Ops",
                },
            ],
        },
    ],
)
    
for instance in instances:
    print(f'This is the EC2 instance id : "{instance.id}" for the Ops environment is launched')
    
    instance.wait_until_running()
    
    print(f'The EC2 instance id : "{instance.id}" is running')
    print("")



import boto3

ec2 = boto3.client("ec2")

#Environment tag with the value Ops, like that it will find the right instance
tags={"Name": "tag:environment","Values": ["Ops"]}

#looking for the specified instance that are running
running={"Name": "instance-state-name", "Values": ["running"]}

for instances in ec2.describe_instances(Filters=[tags,running])["Reservations"]:
    for instance_id in instances["Instances"]:
        ec2.stop_instances(InstanceIds=[instance_id["InstanceId"]])
        print("The following EC2 instance are stopping: ", [instance_id["InstanceId"]])
