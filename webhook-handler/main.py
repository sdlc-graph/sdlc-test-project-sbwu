import json
import os
from flask import Flask, request, jsonify
from google.cloud import pubsub_v1

app = Flask(__name__)

# --- HARDCODED CONFIGURATION ---
PROJECT_ID = "seven-argo-test"
TOPIC_ID = "ai-metrics-webhook"
# -------------------------------

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@app.route('/webhook', methods=['POST'])
def webhook():

    event_type = request.headers.get('X-GitHub-Event')
    print(f"event_type: {event_type}")
    if event_type != 'pull_request':
        return jsonify({"status": "ignored", "reason": "not a PR event"}), 200

    try:
        data_str = json.dumps(request.json)
        future = publisher.publish(topic_path, data_str.encode("utf-8"))
        message_id = future.result()
        return jsonify({"status": "published", "message_id": message_id}), 200
    except Exception as e:
        print(f"PubSub Error: {e}") # Log error for Cloud Run logs
        return jsonify({"error": str(e)}),  500

    

@app.route('/', )
def hello():

    return "hello", 200

if __name__ == "__main__":
    # Cloud Run injects the PORT environment variable, do not hardcode the port to a fixed number like 8080
    # unless you configure Cloud Run to forward to that specific port.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
