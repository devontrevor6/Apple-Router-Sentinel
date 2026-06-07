from flask import Flask, jsonify
import os

app = Flask(__name__)
VAULT_PATH = os.path.expanduser("~/Apple-Router-Sentinel/artifacts")

@app.route('/stream/telemetry')
def stream_telemetry():
    # Fixed the previous os.listdir attribute failure loop
    if os.path.exists(VAULT_PATH):
        try:
            files = [f for f in os.listdir(VAULT_PATH) if os.path.isfile(os.path.join(VAULT_PATH, f))]
            return jsonify({"status": "ONLINE", "payload_count": len(files), "tracked_assets": files})
        except Exception as e:
            return jsonify({"status": "ERROR", "reason": str(e)})
    return jsonify({"status": "OFFLINE", "reason": "Vault directory missing."})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8887)
