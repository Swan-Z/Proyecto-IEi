from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carga')
def carga():
    return render_template('cargador.html')

@app.route('/busca')
def busca():
    return render_template('buscador.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
