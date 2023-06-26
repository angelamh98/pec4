# Nombre del Proyecto

Análisis de Sentimientos en Twitter

## Descripción

Este proyecto realiza un análisis de sentimientos en tweets utilizando técnicas de procesamiento de texto y visualización de datos. El código se encarga de realizar el preprocesamiento de los textos, eliminando URLs, caracteres especiales y convirtiéndolos a minúsculas. Además, se eliminan las stopwords (palabras vacías) y se calculan las frecuencias de términos y el vocabulario.

## Requisitos

Python 3.x
Librerías necesarias:
zipfile
os
csv
re
collections
wordcloud
matplotlib
## Instalación

Clona o descarga este repositorio.

Navega hasta el directorio del proyecto.

cd tu_repositorio

Opcionalmente, se recomienda crear y activar un entorno virtual.

python3 -m venv env
source env/bin/activate

Instala las dependencias del proyecto.

pip install -r requirements.txt


## Uso

Asegúrate de estar en el directorio raíz del proyecto.
Ejecuta el archivo principal.

python main.py

##Estructura del Proyecto

main.py: Archivo principal del proyecto que contiene el código para realizar el análisis de sentimientos en los tweets.
data/: Directorio que almacena los datos utilizados por el programa.
tests/: Directorio que contiene los tests unitarios para el código.


