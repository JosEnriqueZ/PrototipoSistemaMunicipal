import os
import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
 
load_dotenv()
servidor    = os.getenv("Servidor")
nombre_db   =os.getenv("nombre_db")
usuario     =os.getenv("Usuario")
password    = os.getenv("Password")

engine = create_engine("mssql+pyodbc://"+usuario+":"+password+"@"+servidor+"/"+nombre_db+"?driver=ODBC+Driver+17+for+SQL+Server")
con=engine.connect()

query = 'SELECT * FROM dbo.Trabajador;'

df = pd.read_sql(query, con)
print(df.head())
##df.head()
