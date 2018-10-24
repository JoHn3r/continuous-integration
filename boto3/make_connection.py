import boto3
#connect to the required ressource
s3 = boto3.resource('s3')

#S3 example, so we list the buckets
for bucket in s3.buckets.all():
    print(bucket.name)