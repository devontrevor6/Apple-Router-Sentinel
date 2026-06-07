import os
import time
from datetime import datetime
from flask import Flask, render_template_string, redirect

app = Flask(__name__)

VAULT_PATH = os.path.expanduser("~/Apple-Router-Sentinel/artifacts")
CHECKIN_FILE = os.path.expanduser("~/Apple-Router-Sentinel/.dms_checkin")

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>SENTINEL DASHBOARD</title>
    <style>
        body { background: #050505; color: #00ff41; font-family: 'Courier New', monospace; padding: 20px; }
        h1, h2 { color: #ffffff; text-shadow: 0 0 5px #00ff41; }
        .accordion { background-color: #111; color: #00ff41; cursor: pointer; padding: 15px; width: 100%; border: 1px solid #333; text-align: left; font-weight: bold; margin-top: 5px; font-family: monospace; }
        .active, .accordion:hover { background-color: #222; border-color: #00ff41; }
        .panel { padding: 0 18px; display: none; background-color: #0a0a0a; border: 1px solid #222; border-top: none; overflow: hidden; }
        ul { list-style-type: square; margin: 10px 0; }
        li { margin: 5px 0; }
        a { color: #33ff33; text-decoration: none; }
        a:hover { text-decoration: underline; text-shadow: 0 0 3px #33ff33; }
        .btn { background: #111; color: #ff3333; border: 1px solid #ff3333; padding: 10px 20px; cursor: pointer; font-family: monospace; font-weight: bold; }
        .btn:hover { background: #ff3333; color: #000; }
    </style>
</head>
<body>
    <h1>SNTL TELEMETRY CORE</h1>
    <hr style="border-color: #333;">
    
    <h2>ARCHIVE VAULT STORAGE</h2>
    {% for cat_id, cat in data.items() %}
        <button class="accordion">{{ cat.label }} ({{ cat.size }} bytes)</button>
        <div class="panel">
            {% if cat.files %}
                <ul>
                {% for file in cat.files %}
                    <li><a href="http://127.0.0.1:8886/download/{{ file }}">{{ file }}</a></li>
                {% endfor %}
                </ul>
            {% else %}
                <p style="color: #666; font-style: italic;">No telemetry assets indexed.</p>
            {% endif %}
        </div>
    {% endfor %}
    
    <br><br>
    <h2>DEAD MAN'S SWITCH</h2>
    <form action="/reset_dms" method="POST" style="display: inline;">
        <button type="submit" class="btn">RESET INTERVAL TIMESTAMP</button>
    </form>

    <script>
        var acc = document.getElementsByClassName("accordion");
        for (var i = 0; i < acc.length; i++) {
            acc[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var panel = this.nextElementSibling;
                if (panel.style.display === "block") {
                    panel.style.display = "none";
                } else {
                    panel.style.display = "block";
                }
            });
        }
    </script>
</body>
</html>
"""

def get_vault_data():
    categories = {
        "Network": {"label": "NETWORK INFRASTRUCTURE", "files": [], "size": 0},
        "Comms": {"label": "ENCRYPTED COMMS", "files": [], "size": 0},
        "Intel": {"label": "GATHERED INTEL", "files": [], "size": 0}
    }

    if os.path.exists(VAULT_PATH):
        for f in os.listdir(VAULT_PATH):
            path = os.path.join(VAULT_PATH, f)
            if os.path.isfile(path) and not f.startswith('.'):
                filename_lower = f.lower()
                f_size = os.path.getsize(path)
                
                if "network" in filename_lower or "matrix" in filename_lower or "block" in filename_lower:
                    categories["Network"]["files"].append(f)
                    categories["Network"]["size"] += f_size
                elif "proof" in filename_lower or "report" in filename_lower or "intel" in filename_lower:
                    categories["Intel"]["files"].append(f)
                    categories["Intel"]["size"] += f_size
                else:
                    categories["Comms"]["files"].append(f)
                    categories["Comms"]["size"] += f_size
                    
    return categories

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, data=get_vault_data())

@app.route('/reset_dms', methods=['POST'])
def reset_dms():
    os.makedirs(os.path.dirname(CHECKIN_FILE), exist_ok=True)
    with open(CHECKIN_FILE, "w") as f:
        f.write(datetime.now().isoformat())
    return redirect('/')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888)
