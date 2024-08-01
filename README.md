# XLF-XLIFF Translator

This project is an XLF - XLIFF file translator with XML structure. It allows you to take the content of `<source></source>` and translate it within the `<target></target>` property. This makes the translation task easier, less tedious, and more automated.

## Features

- Translates the content of `<source>` to `<target>` using Google Translator.
- Handles files with `.xml`, `.xlf`, `.xliff` extensions.
- Automates the translation process while maintaining the XML structure.
- Excellent choice for i18n.
- Working perfect for Angular Internationalization. 

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


## Detailed Explanation of the Script

The `translator.py` script includes a function called `process_xliff` that takes an XLIFF file and translates its content from one language to another. To use this function, you need to provide four arguments:

1. **`file_path`**: The path to the XLIFF file you want to translate.
2. **`source_lang`**: The language code of the original content found in the `<source>` elements.
3. **`target_lang`**: The language code to which you want to translate the content of the `<source>` elements.
4. **`file_extension`**: The extension of the input file (can be `xml`, `xlf`, `xliff`).

### `source_lang` and `target_lang`

These properties specify the source and target languages for translation. They are used in the `translate_text` function to perform the translation using the Google Translator API.

```python
def translate_text(text, source_lang, target_lang):
    # Translates text from source_lang to target_lang using GoogleTranslator
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return text  # Fallback to source text if translation fails
```

### `file_extension`

This property specifies the extension of the file to be processed. The function checks if the input file has the correct extension before proceeding with the translation.

```python
def process_xliff(file_path, source_lang, target_lang, file_extension):
    # Processes an XLIFF file, translating text from source_lang to target_lang

    file_extension = file_extension.lower()

    # Check if the file has a valid extension
    if not file_path.endswith(f'.{file_extension}'):
        raise ValueError(f"The file must be an XLIFF file with a .{file_extension} extension.")
```

### Verifications Performed

1. **File Extension Verification**:
   The function verifies that the input file has the specified extension (`.xml`, `.xlf`, `.xliff`). If it does not match, it raises an exception.

   ```python
   if not file_path.endswith(f'.{file_extension}'):
       raise ValueError(f"The file must be an XLIFF file with a .{file_extension} extension.")
   ```

2. **File Reading**:
   The function attempts to read the file's content. If an error occurs during reading, it catches the error and displays an error message.

   ```python
   try:
       with open(file_path, 'rb') as file:
           xml_content = file.read()
   except Exception as e:
       print(f"Error reading file '{file_path}': {e}")
       return None
   ```

3. **XML Content Parsing**:
   The function attempts to parse the file's content as XML. If parsing fails due to a syntax error, it catches the error and displays an error message.

   ```python
   try:
       root = etree.fromstring(xml_content)
   except etree.XMLSyntaxError as e:
       print(f"Error parsing XML: {e}")
       return None
   ```

4. **Iterating Through `trans-unit` Elements**:
   The function iterates through all `<trans-unit>` elements in the XML file and checks if the `<source>` and `<target>` elements exist.

   - If the `<target>` element does not exist, it creates a new one and adds it after the `<source>` element.
   - If the `<target>` element is empty, it translates the content of `<source>` and copies it to `<target>`.

   ```python
   for trans_unit in root.xpath(".//ns:trans-unit", namespaces=ns):
       source = trans_unit.find('ns:source', namespaces=ns)
       target = trans_unit.find('ns:target', namespaces=ns)

       if source is not None:
           source_text = source.text

           if target is None:
               target = etree.Element('target')
               source.addnext(target)

           if target.text is None:
               translated_text = translate_text(source_text, source_lang, target_lang)
               target.text = translated_text

               for elem in source:
                   new_elem = etree.Element(elem.tag, attrib=elem.attrib)
                   new_elem.text = elem.text
                   target.append(new_elem)
                   if elem.tail:
                       translated_tail = translate_text(elem.tail, source_lang, target_lang)
                       new_elem.tail = translated_tail
   ```

5. **Writing the Modified File**:
   The function writes the modified XML content to a new file with the suffix `.modified` in its name. If an error occurs during writing, it catches the error and displays an error message.

   ```python
   output_path = file_path.replace(f".{file_extension}", f".modified.{file_extension}")
   try:
       tree.write(output_path, encoding='utf-8', xml_declaration=True, pretty_print=True)
   except Exception as e:
       print(f"Error writing file '{output_path}': {e}")
       return None
   ```

### Example of Use

```python
file_path = './files/messages-example.xlf'
source_lang = 'english'
target_lang = 'spanish'
file_extension = 'xlf'  # Can be 'xml', 'xlf', 'xliff'
output_path = process_xliff(file_path, source_lang, target_lang, file_extension)

if output_path:
    print(f"Output file created: {output_path}")
else:
    print("Failed to create output file.")
```

## Run the script
To run the script, use the following command:
```bash
python translator.py
```

## Example XML Structure
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">
  <file source-language="en" datatype="plaintext" original="ng2.template">
    <body>
      <trans-unit id="1694073859578581253" datatype="html">
        <source>Dividend and Stock Returns Forecaster</source>
        <target></target>
        <context-group purpose="location">
          <context context-type="sourcefile">src/app/pages/calculator/calculator.component.html</context>
          <context context-type="linenumber">4,5</context>
        </context-group>
      </trans-unit>
    </body>
  </file>
</xliff>
```


---
## Explicación en Español

Este proyecto es un traductor de archivos XLF - XLIFF con estructura XML. Permite tomar el contenido de `<source></source>` y traducirlo dentro de la propiedad `<target></target>`. Esto hace que la tarea de traducción sea más sencilla, menos tediosa y más automatizada.

## Características

- Traduce el contenido de `<source>` a `<target>` utilizando Google Translator.
- Maneja archivos con extensiones `.xml`, `.xlf`, `.xliff`.
- Automatiza el proceso de traducción manteniendo la estructura XML.
- Excelente elección para i18n.
- Funcionando de manera perfecta con "Angular Internationalization".

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

## Estructura de Ejemplo XML

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">
  <file source-language="en" datatype="plaintext" original="ng2.template">
    <body>
      <trans-unit id="1694073859578581253" datatype="html">
        <source>Dividend and Stock Returns Forecaster</source>
        ...
      </trans-unit>
    </body>
  </file>
</xliff>
```
