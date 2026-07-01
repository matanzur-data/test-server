from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def catch_all(path):
    data = request.get_json(silent=True)
    print("=== SHOPIFY WEBHOOK ===")
    print(json.dumps(data, indent=2))
    print("======================")
    return jsonify({"predicted_ltv": 200 , "value" : json.dumps(data, indent=2) }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
