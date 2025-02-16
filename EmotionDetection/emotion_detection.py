import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    max_score = 0
    max_key = None
    for k,v in emotions.items():
        if v > max_score:
            max_score = v
            max_key = k

    return {
    'anger': emotions['anger'],
    'disgust': emotions['disgust'],
    'fear': emotions['fear'],
    'joy': emotions['joy'],
    'sadness': emotions['sadness'],
    'dominant_emotion': max_key
    }