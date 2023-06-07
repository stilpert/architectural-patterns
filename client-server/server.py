from flask import Flask, request
app = Flask(__name__)

curr_animal_sound = 'meow'


@app.route('/get_sound', methods=['GET'])
def get_sound():
    return curr_animal_sound


@app.route('/set_sound', methods=['POST'])
def set_sound():
    global curr_animal_sound
    new_sound = request.json['sound']
    curr_animal_sound = new_sound
    return {'ok': 'ok'}


if __name__ == '__main__':
    app.run(port=3000)
