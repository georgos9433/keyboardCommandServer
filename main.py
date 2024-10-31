from flask import Flask, request
from pynput import keyboard
import time

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
    

    if keys[1]=='up' :
        for i in range(40):
            keyboard.Controller().press(getattr(keyboard.Key, keys[0]))
            keyboard.Controller().press(keyboard.Key.up)
            keyboard.Controller().release(getattr(keyboard.Key, keys[0]))
            keyboard.Controller().release(keyboard.Key.up)
    elif keys[1]=='down':
        for i in range(40):
            keyboard.Controller().press(getattr(keyboard.Key, keys[0]))
            keyboard.Controller().press(keyboard.Key.down)
            keyboard.Controller().release(getattr(keyboard.Key, keys[0]))
            keyboard.Controller().release(keyboard.Key.down)
    else:
        keyboard.Controller().press(getattr(keyboard.Key, keys[0]))
        keyboard.Controller().press(keyboard.KeyCode.from_char(keys[1]))
        keyboard.Controller().release(getattr(keyboard.Key, keys[0]))
        keyboard.Controller().release(keyboard.KeyCode.from_char(keys[1]))


    # if keys[1]=='up' :
    #     keyboard.Controller().press(keyboard.Key.up)
    # elif keys[1]=='down':
        
    #     keyboard.Controller().press(keyboard.Key.down)
    # else:
    #     keyboard.Controller().press(keyboard.KeyCode.from_char(keys[1]))

    # # do something here that requires the "Ctrl" + "Shift" + "A" keys to be pressed

    # # release the keys
    # keyboard.Controller().release(getattr(keyboard.Key, keys[0]))
    # if keys[1]=='up' :

    #     keyboard.Controller().release(keyboard.Key.up)
    # elif keys[1]=='down':
    #     keyboard.Controller().release(keyboard.Key.down)
    # else:
    #     keyboard.Controller().release(keyboard.KeyCode.from_char(keys[1]))

    
    

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



if __name__ == "__main__":
    app.run(host='0.0.0.0')



