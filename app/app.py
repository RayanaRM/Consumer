from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Simula o consumo de CPU
    for _ in range(10000000):
        os.urandom(100)

    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=90)
