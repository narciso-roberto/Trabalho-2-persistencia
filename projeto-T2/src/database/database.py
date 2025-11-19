from sqlmodel import SQLModel, create_engine
import sqlite3
from sqlalchemy import event, Engine

engine = create_engine("sqlite:///database.db")

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:
        cursos = dbapi_connection.cursor()
        cursos.execute("PRAGMA foreign_keys=ON")
        cursos.close()