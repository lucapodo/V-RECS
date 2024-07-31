import chardet
import csv
import pandas as pd
import re
# from huggingface_hub import InferenceClient
# import os
# import requests
# import altair_viewer
# import altair as alt
# from newtonmetrics.vegazero.VegaZero2VegaLite import VegaZero2VegaLite 
# from newtonmetrics.newton.newton import Newton 
# n = Newton()


def detect_encoding(file):
    """Detect the encoding of a file."""
    raw_data = file.read(10000)
    file.seek(0)
    result = chardet.detect(raw_data)
    return result['encoding']

def detect_separator(file, encoding):
    """Detect the delimiter of a file."""
    file.seek(0)
    sample = file.read(10000).decode(encoding)
    sniffer = csv.Sniffer()
    delimiter = sniffer.sniff(sample).delimiter
    file.seek(0)  
    return delimiter

# def file_selector(folder_path='.'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox('Select a file', filenames)
#     return os.path.join(folder_path, selected_filename)

def get_nl(text, pattern):
    try:
        match = re.search(pattern, text, flags=re.DOTALL)
        return match.group(1).strip()
    except:
        return False
    
def insert_substring_before_encoding(main_string, substring):
    index = main_string.find("encoding")
    if index == -1:
        return main_string + substring
    else:
        return main_string[:index] + substring + main_string[index:]
    

def map_dtype_to_custom(dtype):
        if pd.api.types.is_numeric_dtype(dtype):
            return 'numeric'
        elif pd.api.types.is_string_dtype(dtype):
            return 'categorical'
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return 'temporal'
        else:
            return 'other'

