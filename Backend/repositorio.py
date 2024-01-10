from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY
from flask import jsonify

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class Repositorio:
    def fetchData(tablename):
        usuarios = supabase.table(tablename).select('*').execute()
        return usuarios
    
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
        respuesta = supabase.table(tablename).select('*').eq('id', id).execute()
        return respuesta.data
    def fetchDataByNames(tablename, name):
        respuesta = supabase.table(tablename).select('*').eq('nombre', name).execute()
        return respuesta.data
    
    def fetchDataByNameAndAddress(name, address):
        # Realiza una consulta a la tabla 'tablename' donde 'nombre' sea igual a 'name' y 'direccion' sea igual a 'address'
        respuesta = supabase.table('centro_educativo').select('*').eq('nombre', name).eq('direccion', address).execute()

        # Retorna los datos obtenidos de la consulta
        return respuesta.data
    
    
    def fetchBusqueda(codigo_postal, en_provincia, nombre_localidad, tipo):
        try:
            
            centros = supabase.table('centro_educativo').select('*').eq('codigo_postal', codigo_postal).execute()
            tipo_centro = supabase.table('centro_educativo').select('*').eq('tipo', tipo).execute()

            provincia = supabase.table('provincia').select('*').ilike('nombre', en_provincia).execute()
            localidad = supabase.table('localidad').select('*').ilike('nombre', nombre_localidad).eq('en_provincia', provincia.data[0]['nombre']).execute()

            coincidencia = supabase.table('centro_educativo').select('*').eq('id_localidad', localidad.data[0]['id']).eq('tipo', tipo_centro.data[0]['tipo']).eq('codigo_postal', centros.data[0]['codigo_postal']).execute()
            if (coincidencia is None):
                raise ValueError('No se encontraron coincidencias')
            print(coincidencia.data)
            return coincidencia.data
        except Exception as e:
            print(e)
            return None


    
    