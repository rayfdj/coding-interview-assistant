import logging

from flask import Flask, render_template, request, jsonify
from ai_interview_companion import generate_solution

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/handle_transcript', methods=['POST'])
def handle_transcript():
    data = request.get_json()
    language = data.get('language', '')
    logging.debug(f"Received language: {language}")
    transcript = data.get('transcript', '')
    logging.debug(f"Received transcript: {transcript}")

    result = generate_solution(language, transcript)
    logging.debug(f"Processed result: {result}")

    return jsonify(result=result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
