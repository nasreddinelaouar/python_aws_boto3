#Create an aws ebs volume from a snapshot
import boto3

ec2_client = boto3.client("ec2")
ec2_client.delete_snapshot(SnapshotId = 'snap-snapshotID')
     