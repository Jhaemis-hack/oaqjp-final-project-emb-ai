''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("My Emotion Detector app")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args["textToAnalyze"]

    if text_to_analyze is None or text_to_analyze == "":
        return "Invalid text! Please try again!.", 400

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion ") is None:
        return "Invalid text! Please try again!.", 400

    emotion_metrics = ""

    for key, value in result.items():
        if key == "dominant_emotion":
            emotion_metrics += f". The dominant emotion is {value}."
        else:
            emotion_metrics += f", '{key}': {value}"

    return f"For the given statement, the system response is {emotion_metrics}", 200

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
