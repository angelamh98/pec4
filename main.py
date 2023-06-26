# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""


# Created on Sun Jun 25 22:05:44 2023

# @author: angela
# """

import zipfile
import os
import csv
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# PARTE DE CONTROL Y REVISIÓN DEL DATASET

# En primer lugar, se extrae el archivo en la carpeta data

# Ruta del archivo comprimido
zip_file_path = "twitter_reduced.zip"

# Directorio de destino para extraer los archivos
extract_dir = "data"

# Descomprimir el archivo ZIP
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(extract_dir)

# Listar los archivos extraídos
extracted_files = os.listdir(extract_dir)
print("Archivos extraídos:", extracted_files)

# Ahora se lee el archivo para crear el diccionario

# Ruta del archivo CSV
csv_file_path = "data/twitter_reduced.csv"

# Lista para almacenar los diccionarios de cada fila
dataset = []

# Leer el archivo CSV y convertirlo en una lista de diccionarios
with open(csv_file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dataset.append(row)

# Mostrar los 5 primeros registros del dataset
print("\nPrimeras 5 filas del diccionario creado:\n")
for i in range(5):
    print(dataset[i])

# EJERCICIO 2.1 - Realizar el preprocesamiento de los textos

# Función para realizar el preprocesamiento de un texto
def preprocess_text(text):
    # Eliminar URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Eliminar caracteres especiales no ASCII y símbolos
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    text = re.sub(r"[^\w\s]", "", text)

    # Convertir el texto a minúsculas
    text = text.lower()

    return text

# Aplicar el preprocesamiento a todos los textos en el dataset
for row in dataset:
    row['text'] = preprocess_text(row['text'])

# Mostrar los 5 primeros registros del dataset después del preprocesamiento
print("\nPrimeras 5 filas del diccionario creado una vez procesado:\n")
for i in range(5):
    print(dataset[i])

# EJERCICIO 2.2 - Quitar las stopwords

# Lista de stopwords
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

# Función para eliminar stopwords de un texto
def remove_stopwords(text):
    # Dividir el texto en palabras individuales
    words = text.split()

    # Filtrar las palabras que no sean stopwords
    filtered_words = [word for word in words if word not in stopwords]

    # Unir las palabras filtradas en un nuevo texto
    filtered_text = " ".join(filtered_words)

    return filtered_text

# Aplicar la eliminación de stopwords a todos los textos en el dataset
for row in dataset:
    row['text'] = remove_stopwords(row['text'])

# Mostrar las 5 últimas filas del dataset después de eliminar las stopwords
print("\nÚltimas 5 filas del diccionario creado, sin stopwords:\n")
last_5_rows = dataset[-5:]
for row in last_5_rows:
    print(row)

# EJERCICIO 3 - Obtener frecuencias de términos y vocabulario

# Lista de diccionarios de frecuencias de términos
term_frequencies = []

# Vocabulario de palabras únicas
vocabulary = []

# Obtener las frecuencias de términos y el vocabulario para cada tuit
for row in dataset:
    text = row['text']
    words = text.split()
    frequencies = dict(Counter(words))
    term_frequencies.append(frequencies)
    row['term_frequencies'] = frequencies
    vocabulary.extend(words)

# Eliminar duplicados del vocabulario
vocabulary = list(set(vocabulary))

print("\nPrimeros 5 elementos del diccionario de frecuencias:\n")
# Mostrar los 5 primeros elementos de la lista de diccionarios de frecuencias
print(term_frequencies[0:5])

# Ordenar alfabéticamente el vocabulario
vocabulary.sort()

print("\nPrimeras 10 palabras del vocabulario:\n")
# Mostrar las 10 primeras palabras del vocabulario
print(vocabulary[:10])

# Mostrar el elemento 20 del dataset
print("\nEl elemento 20 del dataset es:\n")
print(dataset[19])

# Guardar el dataset procesado en un archivo CSV

output_file = 'data/twitter_processed.csv'

# Encabezados de las columnas del archivo CSV
fieldnames = ['sentiment', 'id', 'date', 'query', 'user', 'text', 'term_frequencies']

# Guardar el dataset procesado en el archivo CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dataset)

# PARTE DE ANÁLISIS DE DATOS

# EJERCICIO 5 - Número de clusters
num_clusters = len(set([row['sentiment'] for row in dataset]))
print("\nNúmero de clusters:", num_clusters)

# Verificar si hay elementos vacíos en la columna 'text'
empty_count = sum(1 for row in dataset if row['text'] == '')
percentage_empty = (empty_count / len(dataset)) * 100
print("\nPorcentaje de elementos vacíos en la columna 'text':", percentage_empty)

# Generar word clouds por cluster


# Generar un word cloud para cada cluster
for cluster in set([row['sentiment'] for row in dataset]):
    # Obtener los textos correspondientes al cluster
    texts = [row['text'] for row in dataset if row['sentiment'] == cluster]
    # Unir todos los textos en un solo string
    text_concatenated = ' '.join(texts)
    # Crear el objeto WordCloud y generar el word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_concatenated)
    # Mostrar el word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud - Cluster ' + str(cluster))
    plt.show()

# Generar histograma de valores por cluster
import matplotlib.pyplot as plt

# Obtener los valores de los clusters
cluster_values = {}
for row in dataset:
    sentiment = row['sentiment']
    if sentiment not in cluster_values:
        cluster_values[sentiment] = []
    frequencies = row['term_frequencies']
    total_frequency = sum(frequencies.values())
    cluster_values[sentiment].append(total_frequency)

# Generar histograma para cada cluster
for cluster, values in cluster_values.items():
    plt.hist(values, bins=10, alpha=0.5, label='Cluster {}'.format(cluster))

# Configurar etiquetas y título
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de Valores por Cluster')

# Mostrar leyenda
plt.legend()

# Mostrar el histograma
plt.show()
