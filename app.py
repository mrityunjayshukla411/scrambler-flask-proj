from flask import Flask
from flask import render_template
import random
app = Flask(__name__)

def rand_str_generator():
    randstr = ""
    ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(10):
        randstr += " "
        randstr += ls[random.randint(0,25)]
    return randstr
    

@app.route("/")
def hello_world():
    randstr = rand_str_generator()
    return render_template('index.html' , randstr = randstr)

if __name__ == "__main__":
    app.run(debug=True, port=8000)