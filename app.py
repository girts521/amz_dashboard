from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import json


import sqlite3



app = Flask(__name__)
CORS(app)


@app.route("/data", methods=["GET"])
def handle_data():
    if request.method == "GET":
        conn = sqlite3.connect("./products.db", check_same_thread=False)
        c = conn.cursor()

        product_id = request.args.get('id')
        print("id: ", product_id)
        query = f"""
        SELECT * FROM PriceHistory 
        WHERE product_id={product_id};
        """
        c.execute(query)
        products = c.fetchall()
        print("products: ", products)
        # data = df.to_dict(orient="records")
        conn.close()
        return jsonify(products), 201

@app.route("/data/get_sentiment", methods=["GET"])
def get_sentiment():
    if request.method == "GET":
        conn = sqlite3.connect("./products.db", check_same_thread=False)
        c = conn.cursor()

        product_id = request.args.get('id')
        query = f"""
        SELECT sentiment_array FROM products 
        WHERE id={product_id};
        """
        c.execute(query)
        sentiment_array = c.fetchall()
        print(sentiment_array)
        if sentiment_array[0][0] == None:
            return jsonify("No sentiment"), 404
        sentiment_array = json.loads(sentiment_array[0][0])
        print(sentiment_array)
        conn.close()
        return sentiment_array, 201

if __name__ == "__main__":
    app.run(debug=True)
