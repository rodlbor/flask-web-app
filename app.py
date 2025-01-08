#test
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Change 127.0.0.1 to 0.0.0.0 to allow external access
    app.run(host='0.0.0.0', port=5000)

