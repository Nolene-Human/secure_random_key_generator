# Front end using flask to generate a key

from flask import Flask

import randomkey

app = Flask(__name__)  

'''@app.route('/')
def index():
    return flask.render_template('generate.html')'''

@app.route('/generate', methods=['POST'])
def generate():
    randomkey.generate_key()
    


if __name__=="__main__":
   app.run(host='0.0.0.0')
