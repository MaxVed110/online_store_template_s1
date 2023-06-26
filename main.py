from flask import Flask, render_template

app = Flask(__name__, static_folder='homework_s_10')


@app.route('/')
def index():
    content = {'name': 'Главная'}
    return render_template('index.html', **content)


@app.route('/footwear/')
def footwear():
    content = {'name': 'Обувь'}
    return render_template('footwear.html', **content)


@app.route('/accessories/')
def accessories():
    content = {'name': 'Аксессуары'}
    return render_template('accessories.html', **content)


@app.route('/jackets/')
def jackets():
    content = {'name': 'Куртки'}
    return render_template('jackets.html', **content)


@app.route('/t-shirts/')
def t_shirts():
    content = {'name': 'Футболки'}
    return render_template('t-shirts.html', **content)


if __name__ == '__main__':
    app.run()
