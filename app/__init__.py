"""A tiny Flask app for the DevOps CI/CD project."""

from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>DevOps CI/CD Demo</title><style>
body{font:16px system-ui,sans-serif;max-width:720px;margin:12vh auto;padding:0 24px;color:#172033;background:#f4f7fb}
main{background:white;padding:36px;border-radius:18px;box-shadow:0 12px 36px #18253a12}h1{color:#176b55}.pill{display:inline-block;background:#e5f6ef;color:#176b55;padding:7px 12px;border-radius:99px;font-weight:600}
</style></head><body><main><span class="pill">Deployed successfully</span>
<h1>DevOps CI/CD Demo</h1><p>This app was packaged with Docker and delivered through a GitHub Actions workflow.</p>
<p>Health check: <a href="/health">/health</a></p></main></body></html>"""

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    return app
