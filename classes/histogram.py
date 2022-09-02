import matplotlib.pyplot as plt
import math
import pandas as pd

from classes import Dslr

class Histogram(Dslr):

    def __init__(self) -> None:
        super().__init__()

    def plot_histogram(self, column1, column2):
        x = self._df[column1]
        y = self._df[column2]
        fig, axes = plt.subplots(nrows=1, ncols=2)
        axes[0].plot(x, y)
        axes[1].plot(y, x)

    def show(self):
        plt.tight_layout()
        plt.show()

    def save_figure(self, figure, filename: str):
        figure.savefig(filename)
