from cmath import sqrt
import math
import pandas as pd

class Dslr():

    def __init__(self, data_frame: pd.DataFrame, columns: pd.Index) -> None:
        self._columns = columns
        self._df = data_frame
        self._summary = {}

    def count_rows_sum(self):
        for column in self._columns:
            count = 0
            sum = 0
            for value in self._df[column]:
                if pd.notna(value):
                    count += 1
                    sum += value
            self._summary.update({column: {'Count': count, 'Sum': sum}})

    def mean(self):
        for column in self._columns:
            data_column = self._summary[column]
            count = data_column['Count']
            sum = data_column['Sum']
            mean = sum / count
            data_column.update({**data_column, 'Mean': mean})

    def std(self):
        for column in self._columns:
            data_column = self._summary[column]
            mean = data_column['Mean']
            count = data_column['Count']
            variance = 0
            for value in self._df[column]:
                if pd.notna(value):
                    variance += (value - mean) ** 2
            std = math.sqrt(variance / count)
            data_column.update({**data_column, 'Std': std})

    def min(self):
        for column in self._columns:
            data_column = self._summary[column]
            min = self._df[column][0] # init with first value
            for value in self._df[column]:
                if pd.notna(value):
                    if min > value:
                        min = value
            data_column.update({**data_column, 'Min': min})

    def max(self):
        for column in self._columns:
            data_column = self._summary[column]
            max = self._df[column][0] # init with first value
            for value in self._df[column]:
                if pd.notna(value):
                    if max < value:
                        max = value
            data_column.update({**data_column, 'Max': max})
    
    def count_quartiles(self):
        for column in self._columns:
            for quartile in [0.25, 0.5, 0.75]:
                data_column = self._summary[column]
                count = data_column['Count']
                sorted = self._df[column].sort_values(ascending=True)
                for idx, value in enumerate(sorted):
                    if pd.notna(value) and idx / count >= quartile:
                        if quartile == 0.25:
                            data_column.update({**data_column, '25%': value})
                            break
                        elif quartile == 0.5:
                            data_column.update({**data_column, '50%': value})
                            break
                        else:
                            data_column.update({**data_column, '75%': value})
                            break