from sqlmodel import SQLModel, create_engine
import sqlite3
from sqlalchemy import event, Engine
from dotenv import load_dotenv

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


load_dotenv()

DB_SQLITE = os.getenv("DB_SQLITE")

engine = create_engine(DB_SQLITE)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:
        cursos = dbapi_connection.cursor()
        cursos.execute("PRAGMA foreign_keys=ON")
        cursos.close()