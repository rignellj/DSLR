import pandas as pd

from src import check_args, handle_open, NUMBER_TYPES


class Dslr():

    def __init__(self) -> None:
        self._df: pd.DataFrame
        self.read_data_init()

    def read_data_init(self):
        file = check_args()
        self._df = handle_open(file)
