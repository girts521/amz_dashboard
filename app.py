from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['POST','GET'])
def handle_data():
    if request.method == 'POST':
        data = request.json  # Get JSON data from the request
        return jsonify({'message': 'Data received!', 'data': data}), 201
    if request.method == 'GET':
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
        data = df.to_dict(orient='records')
        return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)