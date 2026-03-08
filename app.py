"""
Simple REST API Flask pour projet DevOps.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Retourne un message de bienvenue en JSON."""
    return jsonify({
        "message": "Bienvenue sur l'API DevOps",
        "version": "1.0"
    })


@app.route("/health")
def health():
    """Retourne le statut de santé de l'application."""
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
