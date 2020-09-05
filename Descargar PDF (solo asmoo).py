import requests
import time
import re
import pandas as pd
import os

def descargar (nombres:list) -> None:
    """Descarga los archivos PDF a la carpeta establecida"""
    descargo = False
    start = time.perf_counter()
    split = []
    directorio = os.getcwd()
    for i in nombres:
        split = i.split(';')
        r = requests.get('http://www.edgeent.com/juegos/hoja_producto/' + split[1])
        contenido = r.content
        print (f"Se esta descargando el archivo: {split[0]} \n")
        descarga = f'{directorio}/Descarga/{split[0]}.pdf'
        with open (descarga, "wb") as f:
            f.write(contenido)
            f.close()
        descargo = True
    if descargo:
        end = time.perf_counter()
        print("La descarga tomo: {}".format(end - start))

def generar_nombres(archivo:str) -> list:
    df = pd.read_excel(archivo)
    lista = []
    codigo = ''
    for i in range(len(df)):
        codigo = df.iloc[i]['Producto'] + ';' + df.iloc[i]['Codigo'] 
        if df.iloc[i]['Editorial'] == 'Edge':
            lista.append(codigo + '.2.2')
        else:
            lista.append(codigo + '.5.2')
    return lista

descargar(generar_nombres('SinNan.xlsx'))