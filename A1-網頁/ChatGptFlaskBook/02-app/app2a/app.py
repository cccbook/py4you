from flask import Flask
from user import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

@app.route('/')
def index():
    return 'This is the home page.'

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
