import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('../photos/databasePhotos/A.jpg','A'),
      ('../photos/databasePhotos/B.jpg','A'),
      ('../photos/databasePhotos/C.jpg','C'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('famouspersons-images','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})