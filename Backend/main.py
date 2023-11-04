from flask import Flask, request, jsonify
import requests
from config import *
from supabase_py import create_client, Client

app = Flask(__name__)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hello', methods=['GET'])
def consultarUsuarios():
    usuarios = supabase.table('usuario').select().execute()
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)