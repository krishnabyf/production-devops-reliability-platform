from flask import Flask, jsonify
import os
import sentry_sdk

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN", ""),
    traces_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "production-devops-reliability-platform",
        "status": "running",
        "environment": os.getenv("ENV", "dev")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/error")
def error():
    raise Exception("Test Sentry incident error")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
