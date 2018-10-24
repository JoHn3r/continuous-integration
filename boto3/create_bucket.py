import boto3

#make connection
s3 = boto3.resource('s3')

#Create bucket

s3.create_bucket(Bucket="sl-boto-bucket",CreateBucketConfiguration={
    'LocationConstraint': 'eu-west-1'})

# data = open('test.jpg', 'rb')
# s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)
#s3.Object('mybucket', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))
