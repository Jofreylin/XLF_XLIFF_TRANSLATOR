# XLF-XLIFF Translator

This project is an XLF - XLIFF file translator with XML structure. It allows you to take the content of `<source></source>` and translate it within the `<target></target>` property. This makes the translation task easier, less tedious, and more automated.

## Features

- Translates the content of `<source>` to `<target>` using Google Translator.
- Handles files with `.xml`, `.xlf`, `.xliff` extensions.
- Automates the translation process while maintaining the XML structure.

## Requirements

- Python 3.x
- `lxml` library
- `deep_translator` library

## Installation

It is recommended to create a virtual environment to manage the project's dependencies.

### Create a virtual environment

#### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### macOS y Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
With the virtual environment activated, install the dependencies:
```bash
pip install -r requirements.txt
```

## Run the script
To run the script, use the following command:
```bash
python translator.py
```


---
## Explicación en Español

Este proyecto es un traductor de archivos XLF - XLIFF con estructura XML. Permite tomar el contenido de `<source></source>` y traducirlo dentro de la propiedad `<target></target>`. Esto hace que la tarea de traducción sea más sencilla, menos tediosa y más automatizada.

## Características

- Traduce el contenido de `<source>` a `<target>` utilizando Google Translator.
- Maneja archivos con extensiones `.xml`, `.xlf`, `.xliff`.
- Automatiza el proceso de traducción manteniendo la estructura XML.

## Requisitos

- Python 3.x
- `lxml` library
- `deep_translator` library

## Instalación

Se recomienda crear un ambiente virtual para gestionar las dependencias del proyecto.

### Crear un ambiente virtual

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### macOS y Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar las dependencias
Con el ambiente virtual activado, instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar el script
Para ejecutar el script, usa el siguiente comando:
```bash
python translator.py
```
