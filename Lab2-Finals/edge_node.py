import requests
import uuid
import random
import time

API_URL = "https://vote-api-739178332753.asia-southeast1.run.app"  

def generate_vote(node_id):
    return {
        "user_id": str(uuid.uuid4()),
        "poll_id": "poll_1",
        "choice": random.choice(["A", "B", "C"]),
        "timestamp": time.time(),
        "time_created": time.time(),
        "edge_id": node_id
    }

def send_vote(vote, retries=3):
    for attempt in range(retries):
        try:
            response = requests.post(API_URL, json=vote, timeout=5)
            print(f"Vote sent: {vote['user_id']} | Choice: {vote['choice']} | Status: {response.status_code}")
            return
        except Exception as e:
            print(f"Transmission failed (attempt {attempt + 1}): {e}")
            time.sleep(1)
    print(f"Vote dropped after {retries} failed attempts.")

def run_edge_node(node_id="node-1"):
    while True:
        vote = generate_vote(node_id)
        send_vote(vote)
        time.sleep(random.uniform(1, 3))

def run_edge_node_with_duplicates(node_id="node-1"):
    while True:
        vote = generate_vote(node_id)
        for i in range(3):
            send_vote(vote)
        time.sleep(random.uniform(1, 3))

if _name_ == "_main_":
    run_edge_node(node_id="node-josh")