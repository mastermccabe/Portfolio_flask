from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template('index.html')

@app.route('/projects')
def success():
    return render_template('projects.html')

@app.route('/about')
def hello():
    return render_template('about.html')


app.run(debug=True)
