from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/footwear/')
def footwear():
    return render_template('footwear.html')


@app.route('/accessories/')
def accessories():
    return render_template('accessories.html')


@app.route('/jakets/')
def jakets():
    return render_template('jakets.html')


if __name__ == '__main__':
    app.run()
