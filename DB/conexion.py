import os
import flet as ft
import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine
#variables entorno
from dotenv import load_dotenv
load_dotenv()

#Base de datos
servidor    = os.getenv("Servidor")
nombre_db   =os.getenv("nombre_db")
usuario     =os.getenv("Usuario")
password    = os.getenv("Password")

engine = create_engine("mssql+pyodbc://"+usuario+":"+password+"@"+servidor+"/"+nombre_db+"?driver=ODBC+Driver+17+for+SQL+Server")
con=engine.connect()
#----------------------------------------------------------
#Busca datos de la tabla de trabajadores
query = 'SELECT * FROM dbo.Trabajador;'
df = pd.read_sql(query, con)


#Muestra todos los trabajadores
print(df.head())
