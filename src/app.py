from flask import Flask, request
import werkzeug

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>DevSecOps Secure Pipeline Demo - MUZDEV</h1>"

@app.route('/execute')
def execute():
    cmd = request.args.get('cmd', 'print("Hello")')
    if cmd == 'Hello':
        return "Hasil Eksekusi: Hello World"
    else:
        return "Hasil Eksekusi: Perintah tidak diizinkan demi keamanan sistem."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
