from flask import Flask, render_template, request, jsonify, redirect, url_for
# from Include.config import Database
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# db = Database()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.get_json()
    usuario = data.get('usuario')
    senha = data.get('senha')

    if not usuario:
        return jsonify({'status': 'error', 'message': 'Preencha o campo usuário'})
    if not senha:
        return jsonify({'status': 'error', 'message': 'Preencha o campo senha'})
    
    # Login sem verificação (apenas para demonstração)
    return jsonify({'status': 'success', 'redirect': url_for('home')})

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    data = request.get_json()
    usuario = data.get('usuario')
    senha = data.get('senha')

    if not usuario:
        return jsonify({'status': 'error', 'message': 'Preencha o campo usuário'})
    if not senha:
        return jsonify({'status': 'error', 'message': 'Preencha o campo senha'})
    
    # Simulação de cadastro bem-sucedido
    return jsonify({'status': 'success', 'redirect': url_for('login')})

@app.route('/')
def root():
    # Rota principal redireciona para login
    return redirect(url_for('login'))

@app.route('/home', methods=['GET'])
def home():
    # Página inicial após login
    return render_template('index.html')

@app.route('/palavras_chave', methods=['GET'])
def palavras_chave():
    return render_template('palavras_chave.html')

@app.route('/lista_usuarios', methods=['GET'])
def lista_usuarios():
    return render_template('lista_usuarios.html')

@app.route('/usuarios', methods=['GET'])
def usuarios():
    return render_template('usuarios.html')

@app.route('/publicacao', methods=['GET'])
def publicacao():
    return render_template('publicacao.html')

@app.route('/recuperar-senha', methods=['GET', 'POST'])
def recuperar_senha():
    if request.method == 'GET':
        return render_template('recuperar-senha.html')
    
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'status': 'error', 'message': 'Preencha o campo email'})
    
    return jsonify({'status': 'success', 'message': f'Um email de recuperação foi enviado para {email}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
