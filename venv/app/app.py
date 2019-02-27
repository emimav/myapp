from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return 'index'

@app.route('/redirect')
def redirectToStatic():
    return redirect('/static/home.html')

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port=3000,debug=True)