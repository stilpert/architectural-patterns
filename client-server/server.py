from flask import Flask, request
app = Flask(__name__)

message = 'my message'


@app.route('/get_message', methods=['GET'])
def get_message():
    return message


@app.route('/set_message', methods=['POST'])
def set_message():
    global message
    new_sound = request.json['sound']
    message = new_sound
    return {'ok': 'ok'}


if __name__ == '__main__':
    app.run(port=3000)
