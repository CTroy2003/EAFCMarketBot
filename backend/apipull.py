from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    print("Received filter data:", data)
    return jsonify({'status': 'success', 'received': data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
