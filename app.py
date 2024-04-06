from flask import Flask, render_template, request
import scripts.test
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/templates/loading', methods=['GET', 'POST'])
def out(potential = None):
    message = dict(request.form)['note']
    print("message" + message)
    potential_diagnoses = scripts.test.out(message)
    print(potential_diagnoses)
    return render_template('/results.html', potential=potential_diagnoses)