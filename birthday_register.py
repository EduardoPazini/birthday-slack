from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

@app.route("/birthday", methods=["POST"])
def register_birthday():
    birth_date = request.form.get("text")


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)