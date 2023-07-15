from flask import Flask, request

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def receive_request():
    return 'Return received!'

if __name__ == '__main__':
    app.run()