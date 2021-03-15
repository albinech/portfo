from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/project.html')
def project():
    return render_template('project.html')


@app.route('/services.html')
def services():
    return render_template('services.html')


@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
