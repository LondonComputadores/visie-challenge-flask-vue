from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/home')
def home_page():
    return render_template('base.html')

@app.route('/form')
def form_page():
    return render_template('form.html')


if __name__ == '__main__':
    app.run()