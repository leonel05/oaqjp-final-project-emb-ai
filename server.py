"""Application server file."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Calling the emotion_detector application with text_to_analyze as the argument
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(str(text_to_analyze))

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
    'anger': {response['anger']}, 'disgust': {response['disgust']}, 
    'fear': {response['fear']}, 'joy': {response['joy']} and 
    'sadness': {response['sadness']}. The dominant emotion is 
    {response['dominant_emotion']}."""

@app.route("/")
def render_index_page():
    """
    GET request to the HTML interface to receive the input text
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
