from flask import Flask, render_template, request
import scripts.test
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/templates/loading', methods=['GET', 'POST'])
def out():
    message = dict(request.form)['note']
    print(message)
    #TODO: processing script
    return "Received"