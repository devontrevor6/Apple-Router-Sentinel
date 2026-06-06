from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def status():
    return "<h1>SNTL PROTECTION: ARMED</h1><p>Status: Monitoring for Intrusion.</p>"

if __name__ == "__main__":
    # Binds locally on alternative interface boundary port 8889
    app.run(host="127.0.0.1", port=8889)
