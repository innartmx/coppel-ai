# RAG - APOC

Este APOC contiene las funcionalidades para leer archivos en PDF, alimentando una base de datos vectorial ([chromadb](https://www.trychroma.com)), para así consumir de forma local un modelo de inteligencia artificial capaz de responder preguntas basadas en los documentos proporcionados.

## Instalación

### 1. Instalar Python

Descargar e instalar python de la página 
[python.org](https://www.python.org/downloads/release/python-3124)

### 2. Instalar dependencias del proyecto

Estando en la carpeta raiz del proyecto, ejecutar el siguiente comando en consola:

```
pip install -r requirements.txt
```

### 3. Instalar modelos de AI

En el paso anterior una de las dependencias instaladas es [ollama](https://www.ollama.com), la cual nos ayudará a descargar los modelos necesarios para nuestro proyecto, para ello es necesario ejecutar los siguientes comandos por separado:

```
ollama pull llama3
ollama pull nomic-embed-text
```

## Ejecutar las funciones

### 1. Cargar documentos en la base de datos de chroma

El primer paso para hacer que funcione nuestro RAG es cargar los documentos relacionados al tema del cual queremos obtener respuestas del modelo. Ésta lògica se encuentra en el archivo [rag_populate_database.py](rag_populate_database.py), el cual podemos ejecutar mediante el siguiente comando, para invocar a su método main():

```
python rag_populate_database.py   
```

Esto creará cargara o actualizará en la base de datos de chromadb los embedings para los documentos que se encuentren en la carpeta "docs"

Si lo que deseamos es resetear la base de datos para cargar en limpio los documentos le pasamos el argumento --reset:

```
python rag_populate_database.py --reset
```

Por defecto se encuentra un documento en la carpeta, si deseamos agregar más documentos se pueden descargar de la siguiente liga:

https://drive.google.com/file/d/1PpNRicAZ2Y8DZgIexlv5ZS6CFqbiyNhI/view?usp=sharing


### 2. Hacerle una pregunta al modelo

En el archivo [rag_chat.py](rag_chat.py) se encuentra la lógica para obtener una respuesta del modelo (llama3), para hacerle una pregunta es necesario invocarlo de la siguiente forma:

```
python rag_chat.py "Tu pregunta"
```

### 3. Ejecutarlo como aplicación web

Para ejecutar el RAG como aplicación web, es necesario ingresr en consola los siguientes comandos:

```
python3 -m venv .venv
. .venv/bin/activate
flask --app app run
```

Esto generará una url local (generarlente en http://127.0.0.1:5000) en la cual se podrá interactuar con el modelo en una interface gráfica de usuario

![Coppel UI](/md/ui.png)