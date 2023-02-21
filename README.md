# PROYECTO INDIVIDUAL Henry
# Descripción del proyecto
Este proyecto tiene como objetivo crear un sistema de recomendación de películas para usuarios, utilizando un modelo de machine learning. Se trabajará con datos de una start-up que provee servicios de agregación de plataformas de streaming.

En este contexto, se asume el rol de Data Scientist y se deben llevar a cabo las siguientes tareas:

Realizar el trabajo de Data Engineer para tener los datos listos para el entrenamiento del modelo.
Desarrollar una API utilizando el framework FastAPI para disponibilizar los datos de la empresa.
Realizar un análisis exploratorio de los datos (EDA).
Entrenar el modelo de machine learning para el sistema de recomendación.
Desplegar el sistema de recomendación en una interfaz gráfica amigable.
Contexto
Se asume que se cuenta con un modelo de recomendación entrenado que ha dado buenas métricas, y se debe llevar ese modelo al mundo real. El ciclo de vida de un proyecto de machine learning contempla desde el tratamiento y recolección de los datos hasta el entrenamiento y mantenimiento del modelo según llegan nuevos datos.
![texto alternativo](https://github.com/luisfer2405/PI_HDT_07_FEB_2023/blob/main/center-image.png)
# Rol a desarrollar
Se comienza a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. El objetivo es crear un sistema de recomendación que aún no ha sido puesto en marcha. Al revisar los datos se encuentra que su madurez es nula, ya que no están transformados y no hay procesos automatizados para la actualización de nuevas películas o series. Se debe empezar desde cero, haciendo un trabajo rápido de Data Engineer y tener un MVP (Minimum Viable Product) para la próxima semana.

Propuesta de trabajo

# Transformaciones
Para el MVP se realizarán las siguientes transformaciones a los datos:

Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)
Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”
De haber fechas, deberán tener el formato AAAA-mm-dd
Los campos de texto deberán estar en minúsculas, sin excepciones
El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)
Desarrollo de la API
Se propone disponibilizar los datos de la empresa utilizando el framework FastAPI. Se implementarán las siguientes consultas:

Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))
Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
# Deployment
Para el deployment se usara Dete:  https://deta.space/discovery/r/xfkhxcse57u6k3fy
y para el modelo de recomendas: https://huggingface.co/spaces/lukmor2405/PI_HDT_07

#Análisis exploratorio de los datos
Una vez que los datos han sido limpiados y transformados, se ha llevado a cabo un análisis exploratorio de los mismos para investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías y detectar algún patrón interesante. Para ello, se han utilizado librerías como pandas profiling, sweetviz, autoviz, entre otras.

#Sistema de recomendación
Una vez que la data es consumible por la API y se ha realizado un buen EDA, se procede a entrenar el modelo de Machine Learning para armar un sistema de recomendación de películas para usuarios. Se espera que este sistema de recomendación sea deployado para tener una interfaz gráfica amigable para ser utilizada, utilizando Gradio o Deta Space para su deployment o bien con alguna solución como Streamlit o algo similar en local.

Video

Se debe crear un video que muestre todo lo que se hizo durante el proyecto, desde las transformaciones:(https://youtu.be/3HsWyEzaWz8)
