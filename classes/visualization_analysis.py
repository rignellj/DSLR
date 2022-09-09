from classes import Analysis
from src.constants import HOUSES, SUBJECTS, P_VALUE

class VisualizationAnalysis(Analysis):

    def __init__(self, category_name) -> None:
        super().__init__()
        self.count_values()
        self._f_test = {}
        self._category_summary = {}
        self._category_name = category_name
        self._ordered_score_dist = {}
        self._score_dist = {}
        self._homogenous_features = set()
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
            for subject in SUBJECTS:
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

    def create_ordered_score_dist(self):
        skip = ['Hogwarts House', 'Index']
        dist1 = self._score_dist[HOUSES[0]]
        dist2 = self._score_dist[HOUSES[1]]
        dist3 = self._score_dist[HOUSES[2]]
        dist4 = self._score_dist[HOUSES[3]]
        save_dict = self._ordered_score_dist

        for subject in SUBJECTS:
            if subject in skip:
                continue
            subject_arr = [
                dist1[subject],
                dist2[subject],
                dist3[subject],
                dist4[subject]
            ]
            for subject_item in subject_arr:
                if subject in save_dict:
                    for key, quartile in subject_item.items():
                        save_dict[subject][key].append(quartile)
                else:
                    save_dict[subject] = {}
                    for key, quartile in subject_item.items():
                        save_dict[subject][key] = [quartile]
        return save_dict
    
    def compare_score_dist(self):
        summary = {}
        homogenous_features = []
        for subject, quartile_data_on_subject in self._ordered_score_dist.items():
            for house in HOUSES:

                # quartile_key = '25%', '50%', '75%'
                for quartile_key in quartile_data_on_subject.keys():

                    # match value is the actual value from dataset
                    match_value = self._category_summary[house][subject][quartile_key]

                    # compare ranges contains min and max values from datasets related to specific
                    # quartile
                    compare_ranges = self._ordered_score_dist[subject][quartile_key]
                    for idx, range_in_house in enumerate(compare_ranges):
                        min_value = range_in_house[0]
                        max_value = range_in_house[1]
                        if match_value >= min_value and match_value <= max_value:
                            if idx == 3:
                                if subject in summary and house in summary[subject]:
                                    summary[subject][house][quartile_key] = 'match'
                                elif subject in summary and house not in summary[subject]:
                                    summary[subject] = {**summary[subject], **{house: {quartile_key: 'match'}}}
                                else:
                                    summary[subject] = {}
                                    summary[subject][house] = {quartile_key: 'match'}
                        else:
                            break
        for k, v in summary.items():
            # all houses
            if len(v) == 4:
                for values in v.values():
                    # all quartiles
                    if len(values) == 3:
                        homogenous_features.append(k)
        self._homogenous_features = set(homogenous_features)

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
