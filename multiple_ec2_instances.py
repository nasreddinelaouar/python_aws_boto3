#Create multile EC2 Instances
import boto3

ec2_resource = boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-Id',
      InstanceType = 't2.micro',
    MaxCount=4,
      MinCount=3)
      