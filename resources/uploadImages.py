import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('./photos/databasePhotos/A.jpg','A.jpg'),
      ('./photos/databasePhotos/B.jpg','B.jpg'),
      ('./photos/databasePhotos/C.jpg','C.jpg'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('signlanguage-images','index/'+ image[1])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})