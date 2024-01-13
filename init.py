import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine

servidor    ='DESKTOP-56AJ9RM\SQLSERVER'
nombre_db   ='CONTROLMUNICIPAL'
usuario     ='sa'
password    ='123'

engine = create_engine("mssql+pyodbc://"+usuario+":"+password+"@"+servidor+"/"+nombre_db+"?driver=ODBC+Driver+17+for+SQL+Server")
con=engine.connect()

query = 'SELECT * FROM dbo.Trabajador;'

df = pd.read_sql(query, con)
print(df.head())
##df.head()
