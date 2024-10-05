from flask import Flask, render_template, send_file, json
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/resume')
def resume():
    return send_file('static/resume.pdf', as_attachment=False)


if __name__ == '__main__':
    app.run(debug=True)
