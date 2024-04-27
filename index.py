from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_sum', methods=['POST'])
def calculate_sum():
    data = request.json
    number1 = data.get('number1')
    number2 = data.get('number2')

    if number1 is None or number2 is None:
        return jsonify({'error': 'Invalid numbers provided'}), 400

    result = number1 + number2
    return jsonify({'result': result}), 200

