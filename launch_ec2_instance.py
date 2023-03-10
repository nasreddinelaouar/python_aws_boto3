#Creating an EC2 Instance using Boto3
import boto3

ec2_resource = boto3.resource("EC2")
ec2_resource.create_instances(ImageId='ami-Id', 
      InstanceType = 't2.micro',
    MaxCount=1,
      MinCount=1)