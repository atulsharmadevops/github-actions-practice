import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    # Just a simple demo using requests
    r = requests.get("https://api.github.com")
    return f"Hello from Docker! GitHub API status: {r.status_code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
