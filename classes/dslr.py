import pandas as pd

class Dslr():

    def __init__(self, data_frame: pd.DataFrame, columns: pd.Index) -> None:
        self._columns = columns
        self._df = data_frame
        self._summary = {}

    def count_rows(self):
        for column in self._columns:
            count = 0
            sum = 0
            for value in self._df[column]:
                if pd.notna(value):
                    count += 1
                    sum += value
            self._summary.update({column: {'Count': count, 'Sum': sum}})

    def count_mean(self):
        for column in self._columns:
            data_column = self._summary[column]
            count = data_column['Count']
            sum = data_column['Sum']
            mean = sum / count
            data_column.update({**data_column, 'Mean': mean})