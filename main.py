from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Lista de sabores e preços
sabores = [
    ("queijo", 49.90),
    ("calabresa", 49.90),
    ("portuguesa", 51.90),
    ("napolitana", 55.90),
    ("4 queijos", 53.90),
    ("brócolis", 45.90),
    ("rúcula", 59.90),
    ("frango com catupiry", 69.90),
]

# Variável global para armazenar o último pedido
ultimo_pedido = {}

@app.route('/')
def home():
    return render_template('index.html', sabores=sabores)

@app.route('/fazer_pedido', methods=['POST'])
def fazer_pedido():
    global ultimo_pedido
    data = request.json
    sabor = data.get('sabor')
    metodo_pagamento = data.get('metodo_pagamento')

    # Verifica se o sabor está na lista
    for s, preco in sabores:
        if s == sabor:
            ultimo_pedido = {
                "sabor": sabor,
                "metodo_pagamento": metodo_pagamento,
                "status": "Preparando"
            }
            return jsonify({
                "mensagem": f"Seu pedido está sendo preparado. Você escolheu a pizza de {sabor}."
            })
    
    return jsonify({"mensagem": "Sabor não encontrado."}), 404

@app.route('/progresso')
def progresso():
    return render_template('progresso.html', pedido=ultimo_pedido)

if __name__ == '__main__':
    app.run(debug=True)
