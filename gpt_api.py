"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"
import sys
from flask_cors import CORS
from flask import Flask, jsonify, request
from gpt_temp import GPT_API
from pdfminer.high_level import extract_text

app = Flask(__name__)
CORS(app)
gpt_app = GPT_API()

@app.route('/')
def index():
    print("here", file=sys.stderr)
    return "Hello, World!"


"EXAMPLE FROM TUTORIAL"
@app.route('/square', methods=['POST'])
def square_number():
    print("kostakis",file=sys.stderr)
    data = request.get_json()
    number = data['number']
    result = number * number
    return jsonify({'result': result})


@app.route('/assistant', methods=['POST'])
def gpt_api():
    data = request.get_json()
    prompt = data['input']

    return jsonify({'result': gpt_app.call(prompt)})

@app.route('/train', methods=['POST'])
def train_assistant():
    data = request.get_json()

    # Extracting text from PDF
    pdf_file = data['file']
    text_pdfminer = extract_text(pdf_file)
    print(text_pdfminer, file=sys.stderr)
    return jsonify({'result': gpt_app.train(text_pdfminer)})

if __name__ == '__main__':
    app.run(debug=True)