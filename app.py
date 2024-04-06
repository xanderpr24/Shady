from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home(name = "Goober"):
    return render_template('/home.html', name=name)
    