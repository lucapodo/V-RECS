import pandas as pd
import src.utils as utils
from typing import Union, Tuple


def load_data(uploaded_file:pd.DataFrame)->Union[str, Tuple[list, pd.DataFrame]]:
    """
    Load and preprocess data from an uploaded file.

    Parameters
    ----------
    uploaded_file : pd.DataFrame
        The uploaded file containing data to be loaded.

    Returns
    -------
    Union[str, Tuple[List[Tuple[str, str]], pd.DataFrame]]
        A tuple containing:
        - A list of tuples with column names and their corresponding custom data types.
        - The loaded DataFrame with columns renamed to lowercase.
        In case of an error, returns a string with the error message.
    """
    
    try:
        encoding = utils.detect_encoding(uploaded_file)
        delimiter = utils.detect_separator(uploaded_file, encoding)


        df = pd.read_csv(uploaded_file, encoding=encoding, on_bad_lines='skip', delimiter=delimiter)
        df = df.rename(columns=lambda x: x.lower())

        column_types = [(col, utils.map_dtype_to_custom(dtype)) for col, dtype in df.dtypes.items()]

        return column_types, df
    except Exception as e:
        return f"Error loading file: {e}"