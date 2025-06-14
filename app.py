from flask import Flask, request, jsonify
from numerology_module import basic_analysis, generate_13_codes, five_elements_analysis

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🎯 Numerology API is running!"

@app.route("/basic", methods=["POST"])
def basic():
    data = request.get_json()
    date_str = data.get("date_str")
    result = basic_analysis(date_str)
    return jsonify(result)

@app.route("/g13", methods=["POST"])
def g13():
    data = request.get_json()
    date_str = data.get("date_str")
    result = generate_13_codes(date_str)
    return jsonify(result)

@app.route("/five", methods=["POST"])
def five():
    data = request.get_json()
    date_str = data.get("date_str")
    result = five_elements_analysis(date_str)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
