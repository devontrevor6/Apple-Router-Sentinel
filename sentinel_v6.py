from flask import Flask, render_template_string, Response
import os
import time
import json
from datetime import datetime

app = Flask(__name__)
RAW_PATH = os.path.expanduser("~/Apple-Router-Sentinel/artifacts")

def event_stream():
    processed_files = set()
    while True:
        if os.path.exists(RAW_PATH):
            # FIXED: Swapped out the incorrect json.listdir call for the native os module function
            current_files = set(os.listdir(RAW_PATH))
            new_files = current_files - processed_files
            
            for f in new_files:
                if not f.endswith('.tmp'):
                    data = {"file": f, "time": datetime.now().strftime('%H:%M:%S')}
                    yield f"data: {json.dumps(data)}\n\n"
                    processed_files.add(f)
        time.sleep(1)

HTML_STREAM_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>SNTL STEADY STREAM</title>
    <style>
        body { background: #050505; color: #00ff41; font-family: 'Courier New', monospace; margin: 20px; }
        #stream-container { height: 80vh; overflow-y: auto; padding: 20px; background: #00440022; border: 1px solid #00ff41; }
        .packet { border-left: 2px solid #00ff41; padding-left: 10px; margin-bottom: 5px; font-size: 0.9rem; opacity: 0.8; }
        .status { color: #ffcc00; }
    </style>
</head>
<body>
    <h2>SNTL // STEADY_DRIP_FEED</h2>
    <div class="status">> ENCRYPTION: ACTIVE | ALARM_BYPASS: ENABLED</div>
    <div id="stream-container"><div id="log"></div></div>
    <script>
        var source = new EventSource("/stream");
        source.onmessage = function(event) {
            var data = JSON.parse(event.data);
            var log = document.getElementById('log');
            var div = document.createElement('div');
            div.className = 'packet';
            div.innerHTML = "[" + data.time + "] INCOMING PACKET >> " + data.file + " ... [OK]";
            log.insertBefore(div, log.firstChild);
        };
    </script>
</body>
</html>"""

@app.route('/')
def index():
    return render_template_string(HTML_STREAM_TEMPLATE)

@app.route('/stream')
def stream():
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    # Binds perfectly to local interface loopback on port 8887
    app.run(host="127.0.0.1", port=8887)
