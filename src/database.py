import pandas as pd
import sqlite3

def get_db_connection():
    """Crée une connexion à la base de données SQLite"""
    return sqlite3.connect('hospital.db')

def query_data(query):
    """Exécute une requête SQL et retourne un DataFrame"""
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df