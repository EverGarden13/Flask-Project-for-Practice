from flask import Flask, request, jsonify
from emotion_app import emotion_predictor

app = Flask(__name__)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    result, status_code = emotion_predictor(text)
    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(debug=True)

