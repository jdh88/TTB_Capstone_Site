from flask import Flask, render_template, request, redirect
from flask import flash

app = Flask(__name__)
#app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pitch/')
def pitch():
    return render_template('pitch.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
  app.run(port=33507)
