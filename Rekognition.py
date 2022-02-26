import boto3
import json
import sys

#Processing image from bucket
def detect_text(photo, bucket):
    client = boto3.client('rekognition', 'us-west-1')

    response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    textDetections = response['TextDetections']
    print('Detected text\n----------')
    for text in textDetections:
        print('Detected text:' + text['DetectedText'])
        print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print('Parent Id: {}'.format(text['ParentId']))
        print('Type:' + text['Type'])
        print()
    return len(textDetections)

#Processing image from local
def detect_labels_local_file(photo):
    client = boto3.client('rekognition', 'us-west-1')

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('Detected labels in ' + photo)
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))

    return len(response['Labels'])


def main():
    bucket = 'new-buck-97'
    photo = 'men.jpg'
    photoo = 'C:/Users\Vishwas\Downloads\Aashik\Sign.jpg'

    #For first method
    text_count = detect_text(photo, bucket)
    print("Text detected: " + str(text_count))

    #for second method
    label_count = detect_labels_local_file(photoo)
    print("Labels detected: " + str(label_count))

if __name__ == "__main__":
    main()