from flask import Flask, request, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            Encryption degree: <input value="0" name="rot">

			<p> Enter Sensitive Message Below:</p> <textarea name="text" rows="4" cols="50">{0}</textarea>
            <input value="Encrypt It" type="submit">
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")
   


@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    new_enc = rotate_string(text,rot)
    
    return form.format(new_enc)
    

app.run()




