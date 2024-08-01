import os 
from lxml import etree
from deep_translator import GoogleTranslator

def translate_text(text, source_lang, target_lang):
    # Translates text from source_lang to target_lang using GoogleTranslator
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return text  # Fallback to source text if translation fails

def process_xliff(file_path, source_lang, target_lang, file_extension):
    # Processes an XLIFF file, translating text from source_lang to target_lang

    file_extension = file_extension.lower()

    # Check if the file has a valid extension
    if not file_path.endswith(f'.{file_extension}'):
        raise ValueError(f"The file must be an XLIFF file with a .{file_extension} extension.")

    # Read the file content
    try:
        with open(file_path, 'rb') as file:
            xml_content = file.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

    # Parse the XML content
    try:
        root = etree.fromstring(xml_content)
    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML: {e}")
        return None

    # Register namespace to properly find elements
    ns = {'ns': 'urn:oasis:names:tc:xliff:document:1.2'}

    # Iterate through trans-unit elements
    for trans_unit in root.xpath(".//ns:trans-unit", namespaces=ns):
        source = trans_unit.find('ns:source', namespaces=ns)
        target = trans_unit.find('ns:target', namespaces=ns)

        # If both elements exist, translate the text from 'source' and copy to 'target'
        if source is not None:
            source_text = source.text

            # If the target element does not exist, create it
            if target is None:
                target = etree.Element('target')
                source.addnext(target)

            #target.clear()  # Clear existing content in target

            # If target is empty
            if target.text is None:
                # Translate the text while preserving XML structure
                translated_text = translate_text(source_text, source_lang, target_lang)
                target.text = translated_text

                # Copy all child elements from source to target, with translations
                for elem in source:
                    new_elem = etree.Element(elem.tag, attrib=elem.attrib)
                    new_elem.text = elem.text
                    target.append(new_elem)
                    if elem.tail:
                        translated_tail = translate_text(elem.tail, source_lang, target_lang)
                        new_elem.tail = translated_tail

    # Write the modified XML content to a new file
    tree = etree.ElementTree(root)
    output_path = file_path.replace(f".{file_extension}", f".modified.{file_extension}")
    try:
        tree.write(output_path, encoding='utf-8', xml_declaration=True, pretty_print=True)
    except Exception as e:
        print(f"Error writing file '{output_path}': {e}")
        return None

    return output_path

# Ejemplo de uso
file_path = './files/messages-example.xlf'
source_lang = 'english'
target_lang = 'spanish'
file_extension = 'xlf'  # Can be 'xml', 'xlf', 'xliff'
output_path = process_xliff(file_path, source_lang, target_lang, file_extension)

# Print the output path if the file was created successfully
if output_path:
    print(f"Output file created: {output_path}")
else:
    print("Failed to create output file.")
