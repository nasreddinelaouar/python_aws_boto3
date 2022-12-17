#Create an aws ebs volume from a snapshot
import boto3

ec2_client = boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-1a',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-snapshotID',
      VolumeType='gp2')