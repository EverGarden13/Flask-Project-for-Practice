import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup authenticator and service
authenticator = IAMAuthenticator('your_api_key')  # Replace with your actual API key
nlp_service = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)

nlp_service.set_service_url('your_service_url')  # Replace with your actual service URL

def emotion_predictor(text):
    if not text.strip():
        return {'error': 'Text input is empty'}, 400

    response = nlp_service.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    emotions = response['emotion']['document']['emotion']
    return {
        'anger': emotions['anger'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'fear': emotions['fear'],
        'disgust': emotions['disgust']
    }
