from sqlmodel import SQLModel, create_engine
import sqlite3
from sqlalchemy import event, Engine

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

engine = create_engine("sqlite:///meu_banco.db")
# database_url = 'postgresql://persistencia:12345@localhost:5432/meu_postgress'


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:
        cursos = dbapi_connection.cursor()
        cursos.execute("PRAGMA foreign_keys=ON")
        cursos.close()