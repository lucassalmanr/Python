from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<body>
    <h1 style="display: flex;" style="justify-self: center;width: 100%;">Curriculo</h1>
    <div style="display: flex;" style="justify-self: center;width: 100%;">
        <p>ouro olitef</p>
        <p>prata oba</p>
        <p>bronze oba</p>
        <p>Conquistas: prata olitef</p>
    </div>
    '''

if __name__ == '__main__':
    app.run(debug=True)
