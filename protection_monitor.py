from flask import Flask, jsonify
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route('/integrity')
def check_integrity():
    uptime = time.time() - START_TIME
    return jsonify({
        "node": "SOVEREIGN_MONITOR",
        "status": "SECURED",
        "uptime_seconds": round(uptime, 2),
        "privilege_zone": "USERSPACE_ARMv8"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8889)
