import pandas as pd
import src.utils as utils
from typing import Union, Tuple


def load_data(uploaded_file:pd.DataFrame)->Union[str, Tuple[list, pd.DataFrame]]:
    try:
        encoding = utils.detect_encoding(uploaded_file)
        delimiter = utils.detect_separator(uploaded_file, encoding)


        df = pd.read_csv(uploaded_file, encoding=encoding, on_bad_lines='skip', delimiter=delimiter)
        df = df.rename(columns=lambda x: x.lower())

        column_types = [(col, utils.map_dtype_to_custom(dtype)) for col, dtype in df.dtypes.items()]

        return column_types, df
    except Exception as e:
        return f"Error loading file: {e}"