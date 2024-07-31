import chardet
import csv
import pandas as pd
import re

def detect_encoding(file)->str:
    """
    Detect the encoding of a file.

    Parameters
    ----------
    file : file object
        The file whose encoding needs to be detected.

    Returns
    -------
    str
        The detected encoding of the file.
    """
    raw_data = file.read(10000)
    file.seek(0)
    result = chardet.detect(raw_data)
    return result['encoding']

def detect_separator(file, encoding:str) -> str:
    """
    Detect the delimiter of a file.

    Parameters
    ----------
    file : file object
        The file whose delimiter needs to be detected.
    encoding : str
        The encoding of the file content.

    Returns
    -------
    str
        The detected delimiter of the file.
    """
    file.seek(0)
    sample = file.read(10000).decode(encoding)
    sniffer = csv.Sniffer()
    delimiter = sniffer.sniff(sample).delimiter
    file.seek(0)  
    return delimiter

def get_nl(text:str, pattern:str) -> str:
    """
    Extract the response subset requested with the pattern from a regex match within the text.

    Parameters
    ----------
    text : str
        The text to search within.
    pattern : str
        The regex pattern to search for.

    Returns
    -------
    str
        The extracted group from the match, or False if no match is found.
    """
    try:
        match = re.search(pattern, text, flags=re.DOTALL)
        return match.group(1).strip()
    except:
        return False
    
def insert_substring_before_encoding(main_string:str, substring:str) -> str:
    """
    Insert the  "encoding" field in the vegazero.

    Parameters
    ----------
    main_string : str
        The main string where the substring should be inserted.
    substring : str
        The substring to insert.

    Returns
    -------
    str
        The modified string with the substring inserted.
    """
    index = main_string.find("encoding")
    if index == -1:
        return main_string + substring
    else:
        return main_string[:index] + substring + main_string[index:]
    

def map_dtype_to_custom(dtype) -> str:
    """
    Map the dataframe dtype to a the custom data type string that is passed to the model as dataset description.

    Parameters
    ----------
    dtype : pandas dtype
        The pandas dtype to map.

    Returns
    -------
    str
        The corresponding custom data type string ('numeric', 'categorical', 'temporal', 'other').
    """

    if pd.api.types.is_numeric_dtype(dtype):
        return 'numeric'
    elif pd.api.types.is_string_dtype(dtype):
        return 'categorical'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'temporal'
    else:
        return 'other'

