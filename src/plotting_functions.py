import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.style.use('ggplot')
import seaborn as sns

def plot_correlation_coefficients(dataframe, title, path_to_file):
    corr = dataframe.corr()
    ax = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True)
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right')
    ax.set_title(title)

    plt.savefig(path_to_file, bbox_inches='tight')

def plot_histogram(series_list, color_list, label_list, x_label, y_label, title, path_to_file, n_bins, ax):
    for series, color, label in zip(series_list, color_list, label_list):
        ax.hist(series, alpha=0.4, color=color, label=label, density=True, bins=n_bins)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()
    ax.set_title(title)
    plt.savefig(path_to_file)

def multiple_scatter_plots(x_list, y_list, color_list, xlabel_list, title_list, path_to_file, ax):
    for idx, (x, y, color, xlabel, title) in enumerate(zip(x_list, y_list, color_list, xlabel_list, title_list)):
        ax[idx].scatter(x, y, color=color)
        ax[idx].set_title(title)
        ax[idx].set_xlabel(xlabel)
    plt.tight_layout
    plt.savefig(path_to_file)



if __name__ == "__main__":
    pass
