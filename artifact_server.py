from flask import Flask, render_template_string, send_from_directory, make_response
import os

app = Flask(__name__)
VAULT_PATH = os.path.expanduser("~/Apple-Router-Sentinel/artifacts")

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>SNTL ARCHIVE DOWNLOADS</title>
    <style>
        body { background: #000; color: #00ff41; font-family: monospace; padding: 20px; }
        ul { list-style-type: square; }
        a { color: #33ff33; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h2>SECURE VAULT ACCESS</h2>
    <hr style="border-color: #00ff41;">
    <ul>
    {% for file in files %}
        <li><a href="/download/{{ file }}">{{ file }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>"""

@app.route('/')
def index():
    files = []
    if os.path.exists(VAULT_PATH):
        files = [f for f in os.listdir(VAULT_PATH) if os.path.isfile(os.path.join(VAULT_PATH, f))]
    return render_template_string(HTML_TEMPLATE, files=files)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(VAULT_PATH, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8886)
