import boto3

imageCount = 0 

def uploadSavedImg():
      s3 = boto3.resource('s3')
      image = '.\photos\\testPhotos\saved_img.jpg','testImage' + str(imageCount) + '.jpg'
      print(image[0])
      print(image[1])
      file = open(image[0],'rb')
      object = s3.Object('test-signlanguage-image-bucket','images/'+ image[1])
      ret = object.put(Body=file,
                        Metadata={'Name':image[1]})

def main():
      s3 = boto3.resource('s3')

      # Get list of objects for indexing
      images=[('./photos/databasePhotos/A/A1.jpg','testImageA2.jpg'),]

      # Iterate through list to upload objects to S3
      for image in images:
            file = open(image[0],'rb')
            object = s3.Object('test-signlanguage-image-bucket','images/'+ image[1])
            ret = object.put(Body=file,
                              Metadata={'Name':image[1]})

if __name__ == "__main__":
    main()
