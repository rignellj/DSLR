import pandas as pd

from src import check_args, handle_open, NUMBER_TYPES

class Dslr():

    def __init__(self) -> None:
        self._columns: pd.Index
        self._df: pd.DataFrame
        self._summary = {}
        self.read_data_init()

    def read_data_init(self):
        file = check_args()
        df = handle_open(file)
        self._df = df.select_dtypes(include=NUMBER_TYPES)
        self._columns = self._df.columns
