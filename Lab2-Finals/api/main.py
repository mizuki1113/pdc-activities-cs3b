from flask import Flask, request, jsonify
from google.cloud import pubsub_v1
import json
import os

app = Flask(__name__)

PROJECT_ID = os.environ.get("GCP_PROJECT", "cs323-voting-system-groupmimic")
TOPIC_ID = "vote-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@app.route("/vote", methods=["POST"])
def receive_vote():
    vote = request.get_json()
    if not vote:
        return jsonify({"error": "Invalid payload"}), 400
    if not all(k in vote for k in ["user_id", "poll_id", "choice"]):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        message = json.dumps(vote).encode("utf-8")
        future = publisher.publish(topic_path, message)
        future.result()
        return jsonify({"status": "accepted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "API is running"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
