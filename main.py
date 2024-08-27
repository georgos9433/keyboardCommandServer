from flask import Flask, request
from pynput import keyboard

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/key', methods=['POST'])
def press_key():
    # get the key to press from the request data
    key = request.data.decode('utf-8')

    # emulate the pressing of the key
    keyboard.Controller().press(keyboard.KeyCode.from_char(key))
    keyboard.Controller().release(keyboard.KeyCode.from_char(key))

    
    return 'Key pressed'


@app.route('/keyCtrl', methods=['POST'])
def press_keyCrtl():
    # the string to simulate
    string = request.data.decode('utf-8')

    # split the string into the individual keys
    keys = string.split('+')
    

    # simulate the pressing of the keys
    keyboard.Controller().press(getattr(keyboard.Key, keys[0]))
    keyboard.Controller().press(keyboard.KeyCode.from_char(keys[1]))

    # do something here that requires the "Ctrl" + "Shift" + "A" keys to be pressed

    # release the keys
    keyboard.Controller().release(getattr(keyboard.Key, keys[0]))
    keyboard.Controller().release(keyboard.KeyCode.from_char(keys[1]))

    return 'Key pressed'



@app.route('/keyShiftAlt', methods=['POST'])
def press_keyShiftAlt():
    # the string to simulate
    string = request.data.decode('utf-8')

    # split the string into the individual keys
    keys = string.split('+')

    # simulate the pressing of the keys
    keyboard.Controller().press(getattr(keyboard.Key, keys[0]))
    keyboard.Controller().press(getattr(keyboard.Key, keys[1]))
    keyboard.Controller().press(keyboard.KeyCode.from_char(keys[2]))

    # do something here that requires the "Ctrl" + "Shift" + "A" keys to be pressed

    # release the keys
    keyboard.Controller().release(getattr(keyboard.Key, keys[0]))
    keyboard.Controller().release(getattr(keyboard.Key, keys[1]))
    keyboard.Controller().release(keyboard.KeyCode.from_char(keys[2]))

    return 'Key pressed'


@app.route("/getMarkers")#questo è solo per sviluppare in contemporanea busyBox
def getMarkers():
    marker={
        "markerId": 'marker1',
        "positionLat": "45.07016911822664",
        "positionLong": "7.681254172297709",
        "infoWindow": "Test1"
    }
    return marker

if __name__ == "__main__":
    app.run(host='0.0.0.0')



