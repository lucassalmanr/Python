from flask import Flask,render_template


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/decorator')
def decorator():    
    return 'é um padrão de projeto Python que permite modificar, estender ou envolver o comportamento de uma função (geralmente uma view function) sem alterar o código original dela <br> vincular URLs a funções específicas (rotas), gerenciar autenticação, manipular requisições/respostas e adicionar funcionalidades extras (como logs ou cache) sem alterar o código original da função <br> @app.route(hello) Isso é outro decorator, mapeando a função abaixo para a rota /hello'
@app.route('/teste')
def teste():
    return render_template('index.html')

@app.route('/solar')
def solar():
    return render_template('Solar.html')

@app.route('/seu_<nome>')
def nome(nome):
    return f'Seu nome é {nome}'


if __name__ == '__main__':
    app.run(debug=True) 