from google.cloud import pubsub_v1, firestore
import json
import time
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

PROJECT_ID = os.environ.get("GCP_PROJECT", "cs323-voting-system-groupmimic")
SUBSCRIPTION_ID = "vote-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)
db = firestore.Client()

def process_vote(message):
    try:
        vote = json.loads(message.data.decode("utf-8"))
        print(f"Received at worker: {vote['user_id']} | Time: {time.time()}")
        doc_id = f"{vote['user_id']}_{vote['poll_id']}"
        db.collection("votes").document(doc_id).set(vote)
        print(f"Processed vote: {vote['user_id']} | Poll: {vote['poll_id']}")
        message.ack()
    except Exception as e:
        print(f"Error processing message: {e}")

def run_worker():
    print("Worker started. Listening for votes...")
    streaming_pull = subscriber.subscribe(subscription_path, callback=process_vote)
    with subscriber:
        try:
            streaming_pull.result()
        except Exception as e:
            streaming_pull.cancel()
            print(f"Worker stopped: {e}")

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Worker running")
    def log_message(self, format, *args):
        pass

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

if __name__ == "__main__":
    t = threading.Thread(target=run_health_server, daemon=True)
    t.start()
    print("Health server started")
    run_worker()
