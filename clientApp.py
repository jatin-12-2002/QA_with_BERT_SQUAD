from flask import Flask,request,jsonify,render_template
from flask_cors import CORS,cross_origin

from bert import QA

app = Flask(__name__)
CORS(app)

model = QA("model")

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    doc = request.json["data"]
    q = request.json["input_question"]
    try:
        out = model.predict(doc,q)
        return jsonify({"result":out})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == "__main__":
    app.run('0.0.0.0',port=8000)