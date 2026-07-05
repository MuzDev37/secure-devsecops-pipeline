from flask import Flask, request
import werkzeug

app = Flask(__name__)

# 1. Pemicu Gitleaks (Secret Leakage / Information Disclosure)
AWS_SECRET_KEY = "AKIAIMZAMB1AEXAMPLE1234567890abcdefghij"
DB_PASSWORD = "super_secret_password_123"

@app.route('/')
def home():
    return "<h1>DevSecOps Pipeline - VULNERABLE KONDISI BEFORE</h1>"

@app.route('/execute')
def execute():
    # 2. Pemicu Bandit (Malicious Commit / Code Injection / Tampering)
    # Menggunakan fungsi eval() dari input query parameter secara buta
    cmd = request.args.get('cmd', 'print("Hello")')
    hasil = eval(cmd) 
    return f"Hasil Eksekusi: {hasil}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
