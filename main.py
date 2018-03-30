from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = int(request.form['text'])
    new_encryption = rotate_string(text, rot)
    return form.format("""<h1>new_encryption</h1>""")


form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                {0}
            }}
        </style>
    </head>
    <body>
      <form method="POST">
        <label>
            I want to encrypt the message:
            <input type="text" name="text"/>
            to the degree of:
            <input type="text" name="rot"/>
            
        </label>
        <input type="submit" value="Encrypt It"/>
    </form>
    </body>
</html> 
"""
@app.route("/")
def index():
    return form.format("")


app.run()