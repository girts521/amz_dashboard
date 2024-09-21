from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

import sqlite3

conn = sqlite3.connect("/home/girts/Documents/scraping/amazon/products.db", check_same_thread=False)
c = conn.cursor()

app = Flask(__name__)
CORS(app)


@app.route("/data", methods=["GET"])
def handle_data():
    if request.method == "GET":
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
        return jsonify(products), 201


if __name__ == "__main__":
    app.run(debug=True)
