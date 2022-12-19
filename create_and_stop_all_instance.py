#!/usr/bin/env python3.7

import boto3


ec2 = boto3.resource("ec2")

instances = ec2.create_instances(
    ImageId="ami-0b5eea76982371e91",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,
    SubnetId = "subnet-0d4aa9f756b19fcd3"
    )
    
for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
    
    instance.wait_until_running()
    
    print(f'EC2 instance "{instance.id}" has been started')
    



ec2 = boto3.resource("ec2")

instance_Id = "i-0af14dede3afc8102"

instance = ec2.Instance(instance_Id)

instance.stop()

for instance in instances:
    print(f'Stopping EC2 instance: {instance.id}')
    
    instance.wait_until_stopped()

    print(f'EC2 instance "{instance.id}" has been stopped')




ec2 = boto3.resource("ec2")

instance_Id = "i-0af14dede3afc8102"

instance = ec2.Instance(instance_Id)

instance.terminate()

for instance in instances:
    print(f'terminating EC2 instance: {instance.id}')
    
    instance.wait_until_terminated()

    print(f'EC2 instance "{instance.id}" has been terminated')
    