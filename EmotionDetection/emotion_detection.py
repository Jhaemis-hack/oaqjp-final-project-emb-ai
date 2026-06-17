import requests, json

def emotion_detector(text):
    emotions = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    
    if text is None:
        return emotions
        
    text_to_analyse = text

    URL="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input= { "raw_document": { "text": text_to_analyse}}

    response =requests.post(URL, json = Input, headers=HEADERS)

    if response.status_code == 200:
        formatted_response= json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        emotion_predicts = list(emotions.values())
        sorted_predicts = sorted(emotion_predicts, reverse=True)
        
        for key, value in emotions.items():
            if value == sorted_predicts[0]:
                emotions["dominant_emotion"] = key
                break

        return emotions
    elif response.status_code == 400:
        return emotions
    else:
        return emotions