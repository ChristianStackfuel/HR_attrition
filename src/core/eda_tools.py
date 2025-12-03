import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cat_pie(df, col, title=None, save_as=None):
    '''
    Pie plot showing class distributions in %, class names in legend.
    
    :param df: DataFrame
    :param col: Name of the column to plot
    :param title: Title for the visual. Default: "Total {col}"
    :param save_as: Beschreibungpath and file name for saving the visual. Default: None
    '''
    crosstab = pd.crosstab(df[col], col, normalize="columns")
    class_rates = crosstab[col]
    if not title: title=f"Total {col}"
    
    fig, ax = plt.subplots()
    ax.pie(class_rates, labels=[f'{p:.1%}' for p in class_rates])
    ax.legend(crosstab.index, title=col, loc='best')
    ax.set_title(title)
    
    if save_as: fig.savefig(save_as)
