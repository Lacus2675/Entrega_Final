# conexion_db.py
"""
import sqlite3
from pathlib import Path

_db_name = None
_connexion = None
_cursor = None

def db():
    
    global _db_name, _connexion, _cursor , _conn
    ruta_archivo = Path(__file__).parent / 'db.txt'

    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    _db_name = archivo.readline().strip()
    
    # Construir ruta completa a la base de datos
    directorio = Path(__file__).parent / 'Bases_De_Datos'
    ruta_db = directorio / _db_name

    _connexion = sqlite3.connect(ruta_db)
    _cursor = _connexion.cursor()
    return _cursor
    """
"""
def close_db():
    
    global _connexion, _cursor
 
    
    _connexion.close()
    _connexion = None
    _cursor = None
 
"""

import sqlite3
from pathlib import Path

_db_name = None
_connexion = None
_cursor = None

def db():
    
    global _db_name, _connexion, _cursor , _conn
    ruta_archivo = Path(__file__).parent / 'db.txt'

    # Si el archivo no existe, lo creamos con el contenido deseado
    if not ruta_archivo.exists():
        ruta_archivo.write_text("inventario1.db\n", encoding='utf-8')

    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    _db_name = archivo.readline().strip()
    
    # Construir ruta completa a la base de datos
    directorio = Path(__file__).parent / 'Bases_De_Datos'
    # Asegurar que el directorio existe
    directorio.mkdir(parents=True, exist_ok=True)
    ruta_db = directorio / _db_name

    _connexion = sqlite3.connect(ruta_db)
    _cursor = _connexion.cursor()
    return _cursor

    