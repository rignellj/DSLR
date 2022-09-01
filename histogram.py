from classes import Histogram
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


X = np.linspace(0, 5, 11)
Y = X ** 2


def intro_to_matplotlib():
    fig = plt.figure()
    axes1 = fig.add_axes([0.1, 0.1, 0.9, 0.9])
    axes1.plot(X, X**2, label='X Squared', color='purple',
               linewidth=2, linestyle='-.', marker=1)
    axes1.plot(X, X**3, label='X Cubed', color='black', lw=2, alpha=0.5,
               ls='-', marker='o', markerfacecolor='grey')
    axes1.set_xlim([0, 2])
    axes1.set_ylim([0, 2])

    # axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

    # axes1.plot(X, Y)
    # axes2.plot(Y, X)

    # axes1.set_xlabel('X label')
    # axes2.set_xlabel('X label')

    # axes1.set_ylabel('Y label')
    # axes2.set_ylabel('Y label')

    # axes1.set_title('Title')
    # axes2.set_title('Title')

    # fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(5, 2))

    # axes[0].plot(X, Y)
    # axes[0].set_title('First')

    # axes[1].plot(Y, X)
    # axes[1].set_title('Second')

    axes1.legend(loc=0)


def seaborn_intro():
    tips = sns.load_dataset('tips')
    # tips.head()

    # sns.distplot(tips['total_bill'], kde=False, bins=30)
    # sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
    # sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
    # sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
    # sns.jointplot(x='total_bill', y='tip', data=tips)

    # sns.pairplot(data=tips)

    sns.rugplot(tips['total_bill'])


def main():
    histogram = Histogram()
    print(histogram._df.describe())

    # histogram.plot_histogram('Arithmancy', 'Astronomy')
    # sns.histplot(histogram._df['Arithmancy'], kde=True)
    # sns.jointplot(x=histogram._df['Arithmancy'],
    #               y=histogram._df['Hogwarts House'])
    # sns.jointplot(x='History of Magic', y='Charms',
    #               data=histogram._df, hue='Hogwarts House', palette='coolwarm')
    # sns.barplot(x='Hogwarts House', y='Charms', data=histogram._df, estimator=np.std)  # type: ignore
    # sns.boxplot(x='Hogwarts House', y='Charms',
    #             data=histogram._df, hue='Best Hand')
    # sns.violinplot(x='Hogwarts House', y='Charms',
    #             data=histogram._df, hue='Best Hand', split=True)
    # sns.stripplot(x='Hogwarts House', y='Herbology',
    #               data=histogram._df, hue='Best Hand', split=True, jitter=True)
    ##################### USE TOGETHER ##################################
    # sns.violinplot(x='Hogwarts House', y='Herbology',
    #                data=histogram._df)
    # sns.swarmplot(x='Hogwarts House', y='Herbology', s=2,
    #               data=histogram._df, dodge=True, color='black')
    ##################### USE TOGETHER ##################################
    # sns.pairplot(data=histogram._df, kind='hex')
    # print(type(histogram._df['Arithmancy']))
    corr = histogram._df.corr()
    # sns.heatmap(corr, annot=True, cmap='coolwarm')
    # sns.heatmap(corr, cmap='magma', linecolor='white', linewidths=1)
    sns.clustermap(corr, cmap='coolwarm', standard_scale=1)
    print(histogram._df)

    histogram.show()


if __name__ == '__main__':
    main()
