from supabase_py import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY
from flask import jsonify

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class Repositorio:
    def getUsuarios():
        usuarios = supabase.table('usuario').select().execute()
        return jsonify(usuarios)
    