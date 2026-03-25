from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    app_name = os.getenv('APP_NAME', 'Flask API')
    app_version = os.getenv('APP_VERSION', '1.0')
    return f"Hello from {app_name} version {app_version}! 🚀"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)