from classes import Analysis
from src.constants import *

class VisualizationAnalysis(Analysis):

    def __init__(self, category_name) -> None:
        super().__init__()
        self.count_values()
        self._f_test = {}
        self._category_summary = {}
        self._category_name = category_name
        self._score_dist = {}
        for house in HOUSES:
            self._score_dist[house] = {}
    
    def define_category_summary(self):
        df = self._df
        for house in HOUSES:
            analysis = Analysis()
            analysis._df = df[df[self._category_name] == house]
            analysis.count_values()
            self._category_summary[house] = analysis._summary

    def define_score_dist(self):
        self.define_category_summary()
        for house_name, house_data in self._category_summary.items():
            print('HOUSE NAME                       ', house_name)
            for subject in SUBJECTS:
                print('SUBJECT!!', subject)
                house_first_q = house_data[subject]['25%']
                house_second_q = house_data[subject]['50%']
                house_third_q = house_data[subject]['75%']
                if isinstance(house_first_q, str) or isinstance(house_second_q, str) or isinstance(house_third_q, str):
                    continue
                self._score_dist[house_name][subject] = {
                    '25%': [house_first_q * (1 - P_VALUE), house_first_q * (1 + P_VALUE)],
                    '50%': [house_second_q * (1 - P_VALUE), house_second_q * (1 + P_VALUE)],
                    '75%': [house_third_q * (1 - P_VALUE), house_third_q * (1 + P_VALUE)]
                }
        print(self._score_dist)

    def count_f_values(self):
        columns_x = SUBJECTS
        columns_y = SUBJECTS
        for iy, col_y in enumerate(columns_y):
            for ix, col_x in enumerate(columns_x):
                if col_x == col_y or ix < iy:
                    continue
                variance_y = self._summary[col_y]['Variance']
                variance_x = self._summary[col_x]['Variance']
                if variance_x == 0:
                    continue
                f_value = variance_y / variance_x
                key = f'{col_y} - {col_x}'
                self._f_test[key] = {'F-Value': f_value}
