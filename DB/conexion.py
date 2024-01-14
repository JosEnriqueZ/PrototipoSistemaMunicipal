import os
import flet as ft
import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine
#variables entorno
from dotenv import load_dotenv
load_dotenv()

def conectar():
    #Base de datos
    servidor    = os.getenv("Servidor")
    nombre_db   =os.getenv("nombre_db")
    usuario     =os.getenv("Usuario")
    password    = os.getenv("Password")
    #cadena de conexion
    #engine = create_engine("mssql+pyodbc://"+usuario+":"+password+"@"+servidor+"/"+nombre_db+"?driver=ODBC+Driver+17+for+SQL+Server")
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+servidor+';DATABASE='+nombre_db+';UID='+usuario+';PWD='+ password)
    return cnxn

def cerrar_conexion(cnxn):
    cnxn.close()
