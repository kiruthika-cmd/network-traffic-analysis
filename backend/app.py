from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    data = []

    decoded = file.stream.read().decode("utf-8").splitlines()
    reader = csv.DictReader(decoded)

    for row in reader:
        bytes_sent = int(row['bytes'])
        status = "Normal"
        if bytes_sent > 1000:
            status = "Suspicious"

        data.append({
            "source": row['source'],
            "destination": row['destination'],
            "bytes": bytes_sent,
            "status": status
        })

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
