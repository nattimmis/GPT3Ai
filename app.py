from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin
import openai
import waitress
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json['data']
    # Load your API key from an environment variable or secret management service
    openai.api_key = "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"

    response = openai.Completion.create(engine="davinci", prompt=data, max_tokens=2000,
      )
    generated_text = response["choices"][0]['text']
    return jsonify({"text" :generated_text}) 

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 33507))
     waitress.serve(app, port=port)
