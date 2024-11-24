from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion_detector():

    text_to_analyze = request.args.get("textToAnalyze")

    if not response.strip():  # Check for blank input
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 400


    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]


    return f"""For the give statement, the system response is 'anger': {anger}, 
            'disgust':{disgust}, 'fear':{fear}, 'joy':{joy} and 'sadness':{sadness}. 
            The dominant emotion is <b>{dominant_emotion}</b>."""



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

