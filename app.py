from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'docker rm mylife'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

