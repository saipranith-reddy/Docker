from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Docker flask."})

@app.route('/health')
def health():
    return jsonify({"message": "Health Page", "status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
