# rodbor
# 2025.1.7 test
# test number 3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

