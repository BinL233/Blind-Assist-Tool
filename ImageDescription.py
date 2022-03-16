import json
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient

def detection(url):
    credential = json.load(open('credential.json'))
    API_KEY = credential['API_KEY']
    ENDPOINT = credential['ENDPOINT']
    cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))


    description = cv_client.describe_image(url)


    for caption in description.captions:
        return f"Image Description: {caption.text}"