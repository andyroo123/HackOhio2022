aws rekognition detect-custom-labels \
  --project-version-arn "arn:aws:rekognition:us-east-1:079644192492:project/SignLangaugeProject/version/SignLangaugeProject.2022-10-08T16.48.46/1665262126043" \
  --image '{"S3Object": {"Bucket": "test-signlanguage-image-bucket","Name": "images/testImageA.jpg"}}' \
  --region us-east-1