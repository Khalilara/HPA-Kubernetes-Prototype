import hashlib
from flask import Flask, jsonify
import logging
import sys

# Logs en STDOUT pour voir ce qui se passe
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/cpu-heavy', methods=['GET'])
def cpu_heavy():
    """Endpoint qui consomme beaucoup de CPU
    Fait 1 million de hash SHA256 - prend ~5-10 secondes
    """
    logger.info("Starting CPU-heavy operation...")
    
    # Calculs CPU intensifs: générer des hashes
    for i in range(1_000_000):
        hashlib.sha256(f"data_{i}".encode()).hexdigest()
    
    logger.info("CPU-heavy operation completed")
    return jsonify({
        "message": "CPU-heavy operation completed"
    }), 200

@app.route('/', methods=['GET'])
def index():
    """Endpoint simple pour tester la connectivité"""
    return jsonify({"message": "HPA Test App is running"}), 200

@app.route('/health', methods=['GET'])
def health():
    """Endpoint pour les probes Kubernetes"""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
