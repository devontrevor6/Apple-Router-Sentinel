from flask import Flask, render_template_string, make_response
import os

app = Flask(__name__)
VAULT_PATH = os.path.expanduser("~/Apple-Router-Sentinel/artifacts")

@app.route('/')
def index():
    files = []
    if os.path.exists(VAULT_PATH):
        files = [f for f in os.listdir(VAULT_PATH) if os.path.isfile(os.path.join(VAULT_PATH, f))]
    HTML_TEMPLATE = """
    <body style="background:#000; color:#0f0; font-family:monospace;">
        <h1>SNTL MASTER ARCHIVE</h1>
        {% for f in files %}
            <p><a href="/view/{{ f }}" style="color:#0f0;">>>> OPEN: {{ f }}</a></p>
        {% endfor %}
    </body>
    """
    return render_template_string(HTML_TEMPLATE, files=files)

@app.route('/view/<path:filename>')
def view_file(filename):
    file_path = os.path.join(VAULT_PATH, filename)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
        response = make_response(content, 200)
        response.mimetype = "text/plain"
        return response
    return "File Not Found", 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
