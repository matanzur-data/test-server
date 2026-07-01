from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def catch_all(path):
    return jsonify({"predicted_ltv": 100}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)