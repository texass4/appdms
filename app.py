from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return 'app renderizado'

@app.get('/teste')
def teste():
    return f"olá"

if __name__ == '__main__':
    app.run()