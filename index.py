from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_sum', methods=['POST'])
def calculate_sum():
    data = request.json
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/', methods = ['GET'])
def done():
    return 'Hello world'