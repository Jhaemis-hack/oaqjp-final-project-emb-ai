import requests, json

def emotion_detector(text):
    if text is None:
        return "At least a word is required"
        
    text_to_analyse = text

    URL="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input= { "raw_document": { "text": text_to_analyse}}

    response =requests.post(URL, json = Input, headers=HEADERS)
    formatted_response= json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    emotion_predicts = list(emotions.values())
    sorted_predicts = sorted(emotion_predicts, reverse=True)
    
    for key, value in emotions.items():
        if value == sorted_predicts[0]:
            emotions["dominant_emotion"] = key
            break
    
    return emotions