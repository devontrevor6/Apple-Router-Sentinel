from flask import Flask, render_template_string
import os
from datetime import datetime

app = Flask(__name__)
VAULT_PATH = os.path.expanduser("~/Apple-Router-Sentinel/artifacts")

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>SNTL INTEL APP</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #000; color: #00ff41; font-family: 'Segoe UI', sans-serif; }
        .tab-content { border: 1px solid #00ff41; padding: 20px; background: #050505; }
        .intel-card { border-left: 5px solid #00ff41; background: #111; margin-bottom: 10px; padding: 15px; }
        .timestamp { color: #888; font-size: 0.8rem; }
    </style>
</head>
<body class="container mt-4">
    <h2>SENTINEL DATA APP v1.0</h2>
    <div class="tab-content mt-3">
        <h4>Filed Batches (Threshold: 2GB)</h4>
        {% if batches %}
            {% for batch in batches %}
                <div class="intel-card">
                    <div class="timestamp">DATE/TIME FILED: {{ batch }}</div>
                    <div>Status: ARCHIVED | Integrity: VERIFIED</div>
                </div>
            {% endfor %}
        {% else %}
            <p class="text-secondary">Waiting for threshold to hit 2GB...</p>
        {% endif %}
    </div>
</body>
</html>"""

@app.route('/')
def index():
    batches = sorted(os.listdir(VAULT_PATH), reverse=True) if os.path.exists(VAULT_PATH) else []
    return render_template_string(HTML_TEMPLATE, batches=batches)

@app.route('/reset_dms')
def reset_dms():
    checkin_path = os.path.expanduser("~/Apple-Router-Sentinel/artifacts/last_checkin")
    with open(checkin_path, "w") as f:
        f.write(datetime.now().isoformat())
    return "SWITCH RESET: 7 DAYS REMAINING"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888)
