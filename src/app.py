from flask import Flask, request
import os

app = Flask(__name__)

# TARGET GITLEAKS: Token rahasia buatan yang menyerupai AWS Key asli
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE-FAKE-KEY-DO-NOT-USE"

@app.route('/')
def home():
    return "<h1>DevSecOps Secure Pipeline Demo</h1>"

@app.route('/execute')
def execute():
    # TARGET BANDIT: Menggunakan fungsi eval() yang sangat rawan eksploitasi
    cmd = request.args.get('cmd', 'print("Hello")')
    return f"Hasil Eksekusi: {eval(cmd)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
