from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY
from flask import jsonify

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class Repositorio:
    def fetchData(tablename):
        usuarios = supabase.table(tablename).select().execute()
        return jsonify(usuarios)
    
    def insertData(tablename, data):
        try:
            clase = supabase.table(tablename).insert(data).execute()
        except Exception as e:
            print(e)
            
    def deleteData(tablename, id):
        clase = supabase.table(tablename).delete().eq('id', id).execute()

    def updateData(tablename, id, data):
        clase = supabase.table(tablename).update(data).eq('id', id).execute()

    def fetchDataById(tablename, id):
        usuarios = supabase.table(tablename).select().eq('id', id).execute()
        return jsonify(usuarios)