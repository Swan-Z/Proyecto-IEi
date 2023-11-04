from flask import Flask, request, jsonify
import requests
from repositorio import *

app = Flask(__name__)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hello', methods=['GET'])
def consultarUsuarios():
    return Repositorio.getUsuarios()

if __name__ == '__main__':
    app.run(debug=True)