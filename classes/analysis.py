from classes import Dslr

import math
import pandas as pd

from src import NUMBER_TYPES


class Analysis(Dslr):

    def __init__(self) -> None:
        super().__init__()
        self._df = self._df[self._df.select_dtypes(include=NUMBER_TYPES).columns.union(['Hogwarts House'])]
        self._summary = {}

    def count_values(self):
        self.count_rows_sum()
        self.mean()
        self.std()
        self.min()
        self.max()
        self.count_quartiles()

    def count_rows_sum(self):
        for column in self._df.columns:
            count = 0
            sum = 0
            for value in self._df[column]:
                if pd.notna(value):
                    count += 1
                    if isinstance(value, (int, float)):
                        sum += value
            self._summary.update({column: {'Count': count, 'Sum': sum}})

    def mean(self):
        for column in self._df.columns:
            data_column = self._summary[column]
            count = data_column['Count']
            sum = data_column['Sum']
            mean = sum / count
            data_column.update({**data_column, 'Mean': mean})

    def std(self):
        for column in self._df.columns:
            data_column = self._summary[column]
            mean = data_column['Mean']
            count = data_column['Count']
            variance = 0
            for value in self._df[column]:
                if pd.notna(value) and isinstance(value, (int, float)):
                    variance += (value - mean) ** 2
            std = math.sqrt(variance / count)
            data_column.update({**data_column, 'Std': std, 'Variance': variance})

    def min(self):
        for column in self._df.columns:
            data_column = self._summary[column]
            min = self._summary[column]['Mean']  # init as mean
            for value in self._df[column]:
                if pd.notna(value) and isinstance(value, (int, float)):
                    if min > value:
                        min = value
            data_column.update({**data_column, 'Min': min})

    def max(self):
        for column in self._df.columns:
            data_column = self._summary[column]
            max = self._summary[column]['Mean']  # init as mean
            for value in self._df[column]:
                if pd.notna(value) and isinstance(value, (int, float)):
                    if max < value:
                        max = value
            data_column.update({**data_column, 'Max': max})

    def count_quartiles(self):
        for column in self._df.columns:
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
