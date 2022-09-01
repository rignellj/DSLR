import pandas as pd

from classes import Analysis


def main():
    analysis = Analysis()
    print(analysis._df.describe())
    analysis.count_rows_sum()
    analysis.mean()
    analysis.std()
    analysis.min()
    analysis.count_quartiles()
    analysis.max()
    print(pd.DataFrame(analysis._summary))


if __name__ == '__main__':
    main()
