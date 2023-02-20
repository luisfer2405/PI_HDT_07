from typing import Union
import pandas as pd
import numpy as np
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List
from fastapi import FastAPI, responses

app = FastAPI()

@app.get("/")
async def root():
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Mi API</title>
        <style>
          /* Estilos para el fondo diagonal */
          body {
            background: linear-gradient(to bottom, #17ff9e, #52f3ff), url('diagonal-background.png');
            background-size: cover;
            background-position: center;
            animation: diagonal-bg 10s linear infinite;
          }
          @keyframes diagonal-bg {
            0% {
              background-position: top;
            }
            100% {
              background-position: bottom;
            }
          }
          /* Estilos para la imagen centrada */
          .center-image {
            width: 65%;
            margin: 0 auto;
            display: block;
          }
          /* Estilos para los botones */
          .button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
          }
          .button {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px;
            cursor: pointer;
          }
          .button:hover {
            opacity: 0.8;
          }

          .fixed-image {
            position: fixed;
            bottom: 0;
            left: 0;
          }
        </style>
      </head>
      <body>
        <img src="https://imgs.search.brave.com/qsD15NWhmXqsVipN4cMK6dBsiPcvp9f2XJPB0p3iLcU/rs:fit:1200:675:1/g:ce/aHR0cHM6Ly93d3cu/cmlvbmVncm8uY29t/LmFyL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDE5LzEyL2piYXJl/aGFtXzE5MTEwNF8w/OTcwX3N0cmVhbWlu/Z18wMDAxLjAuanBn" class="center-image">
        <div class="button-container">
            <a href="/docs" class="button">Ver documentación</a>
            <button class="button" onclick="location.reload()">Recargar página</button>
            <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.githubs.cn%2Fprojects%2F266851712-curso.prep.henry&psig=AOvVaw3QZhfzmQqg_uSBa7m7BfZC&ust=1676927129035000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOjYtsW-ov0CFQAAAAAdAAAAABAD" class="fixed-image">
            <img src="logo.png" class="fixed-image">
        </div>
      </body>
    </html>
    """
    return responses.HTMLResponse(content=html_content)




@app.get("/get_max_duration")
def get_max_duration_pd(release_year: int = None, plataforma: str = None, duration_type: str = None):
    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv('df_plataformas_final.csv')

    # Filtrar el DataFrame
    filtered_df = df[(df['duration_type'] == duration_type) if duration_type is not None else True]
    filtered_df = filtered_df[(filtered_df['release_year'] == release_year) if release_year is not None else True]
    filtered_df = filtered_df[(filtered_df['plataforma'] == plataforma) if plataforma is not None else True]

    # Ordenar el DataFrame y obtener la fila con la duración máxima
    sorted_df = filtered_df.sort_values(by='duration_int', ascending=False)
    max_duration = sorted_df.iloc[0]['title']

    return max_duration

@app.get("/get_score_count/{plataforma}/{ScoreMedio}/{release_year}")
def get_score_count(plataforma: str, ScoreMedio:float , release_year:int):
    df = pd.read_csv('df_plataformas_final.csv')
    filtered_df = df[(df['plataforma'] == plataforma) & (df['ScoreMedio'] >= ScoreMedio) & (df['release_year'] == release_year)]
    cantidad = len(filtered_df)
    return cantidad

@app.get("/get_actor/{plataforma}/{release_year}")
def get_actor(plataforma: str, release_year: int):
    # Generar el diccionario de combinaciones de letras para cada plataforma
    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                         'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                         'hulu': ['h', 'hu', 'hul', 'hulu'],
                         'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    # Buscar la plataforma correspondiente en el diccionario
    platform_full = platform_dict.get(plataforma, plataforma)

    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv('df_plataformas_final.csv')

    # Filtrar por año y plataforma
    filtered_df = df[(df['plataforma'] == platform_full) & (df['release_year'] == release_year)]

    # Contar la cantidad de veces que aparece cada actor en la columna 'cast'
    actor_mas_repetido = df['cast'].str.split(', ', expand=True).stack().value_counts().index[0]

    return actor_mas_repetido


@app.get("/get_count_plataforma/{plataforma}")
def get_count_platform(plataforma):
    # Leer el archivo con los datos
    data = pd.read_csv('df_plataformas_final.csv')
    
    # Filtrar por la plataforma deseada
    data_plataforma = data[data['plataforma'] == plataforma]
    
    # Contar la cantidad de películas
    cantidad_peliculas = len(data_plataforma[data_plataforma['duration_type'] == 'min'])
    
    return cantidad_peliculas


