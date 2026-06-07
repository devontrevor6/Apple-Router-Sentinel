from flask import Flask, render_template_string, redirect
import os
from datetime import datetime

app = Flask(__name__)
VAULT_PATH = os.path.expanduser("~/Apple-Router-Sentinel/artifacts")
CHECKIN_FILE = os.path.expanduser("~/Apple-Router-Sentinel/artifacts/.last_checkin")

def get_vault_data():
    categories = {
        "Network": {"label": "NETWORK INFRASTRUCTURE", "files": [], "size": 0},
        "Comms": {"label": "ENCRYPTED COMMS", "files": [], "size": 0},
        "Intel": {"label": "GATHERED INTEL", "files": [], "size": 0}
    }

    if os.path.exists(VAULT_PATH):
        for f in os.listdir(VAULT_PATH):
            path = os.path.join(VAULT_PATH, f)
            if os.path.isfile(path):
                size = os.path.getsize(path) / 1024  # Size in KB
                f_lower = f.lower()
                if "net" in f_lower:
                    cat = "Network"
                elif "msg" in f_lower or "comm" in f_lower:
                    cat = "Comms"
                else:
                    cat = "Intel"

                categories[cat]["files"].append({"name": f, "size": round(size, 2)})
                categories[cat]["size"] += size
    return categories

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>SNTL COMMAND v7</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background: #000; color: #00ff41; font-family: 'Courier New', monospace; }
        .container { margin-top: 30px; border: 1px solid #00ff41; padding: 20px; background: #050505; }
        .btn-dms { border: 1px solid #ff0000; color: #ff0000; background: transparent; }
        .btn-dms:hover { background: #ff0000; color: #000; }
        .accordion-item { background: #111; border: 1px solid #00ff41; margin-bottom: 10px; }
        .accordion-button { background: #001100; color: #00ff41; font-family: 'Courier New', monospace; }
        .accordion-button:not(.collapsed) { background: #002200; color: #00ff41; border-bottom: 1px solid #00ff41; }
    </style>
</head>
<body>
    <div class="container">
        <div class="d-flex justify-content-between align-items-center">
            <h2>SENTINEL COMMAND v7.0</h2>
            <button onclick="location.href='/reset_dms'" class="btn btn-dms">RESET INTEGRITY DEADLINE</button>
        </div>
        <hr style="background: #00ff41;">
        <p>STATUS: STEADY STREAM ACTIVE | SYSTEM: ARMED</p>

        <div class="accordion" id="sntlMenu">
            {% for id, cat in data.items() %}
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{{id}}">
                        {{ cat.label }} ({% if cat.size > 1024 %}{{ (cat.size/1024)|round(2) }} MB{% else %}{{ cat.size|round(2) }} KB{% endif %})
                    </button>
                </h2>
                <div id="{{id}}" class="accordion-collapse collapse" data-bs-parent="#sntlMenu">
                    <div class="accordion-body">
                        {% if cat.files %}
                            {% for file in cat.files %}
                                <div class="p-2 border-bottom border-secondary d-flex justify-content-between">
                                    <span><strong>FILE:</strong> {{ file.name }}</span>
                                    <span><strong>SIZE:</strong> {{ file.size }} KB</span>
                                </div>
                            {% endfor %}
                        {% else %}
                            <p class="text-muted">No files archived in this category yet.</p>
                        {% endif %}
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, data=get_vault_data())

@app.route('/reset_dms')
def reset_dms():
    os.makedirs(os.path.dirname(CHECKIN_FILE), exist_ok=True)
    with open(CHECKIN_FILE, "w") as f:
        f.write(datetime.now().isoformat())
    return redirect('/')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888)
