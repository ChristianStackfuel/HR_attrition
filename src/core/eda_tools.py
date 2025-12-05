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



def main_correlations(df, threshold=0.2, sort=False):
    """Display a table of numeric column pairs with an 
    absolute linear correlation (after Pearson) >= a givem threshold
    Args:
        df (DataFrame): The dataframe that is to inspect
        threshold (float, optional): The correlation threshold. Defaults to 0.2.
        sort (True or False, optional): If True, sort by correlation index (descending). Defaults to False.
    Returns:
        DataFrame showing the absolute main correlations in df's numeric columns
    """
    import numpy as np
    import pandas as pd
    
    # extract main correlations
    corrs = df.corr(numeric_only=True).abs()
    corrs_upper = pd.DataFrame(np.triu(corrs, k=0), index=corrs.index, columns = corrs.columns)
    main_corrs_tuples = [(x, y, corrs_upper.loc[x, y]) 
                     for x in corrs_upper.columns 
                     for y in corrs_upper.columns 
                     if (not x == y) and corrs_upper.loc[x, y] >= threshold]
    if sort == True:
        main_corrs_tuples = sorted(main_corrs_tuples, key=lambda corr: corr[2], reverse=True)
    
    main_corrs = pd.DataFrame({
        "column_1": [corr[0] for corr in main_corrs_tuples],
        "column_2": [corr[1] for corr in main_corrs_tuples],
        "abs_correlation": [corr[2] for corr in main_corrs_tuples]
    })
    
    if sort: main_corrs = main_corrs.sort_values("abs_correlation", ascending=False)
    
    return main_corrs



def direct_correlations(df, column, sort=True):
    """Display a table all correlation scores (Pearson) with a reference column
    Args:
        df (DataFrame): The dataframe that is to inspect
        key (column name): name of the reference column
        sort (boolean, optional): If True, sort by absolute correlation. 
            Defaults to True.
    Returns:
        DataFrame showing the correlation between each numeric column 
        and the reference column
    """
    import numpy as np
    import pandas as pd
    
    # extract main correlations
    corrs = pd.DataFrame(df.corr(numeric_only=True)[column].sort_values(ascending=False,
                                                                        key=lambda x: abs(x)))
    corrs.columns = [f"correlation with {column}"]
    
    return corrs



def frequency_distribution_plots(df, plotcol, refcol, show=None, save_as=None):
    '''Display 'col vs. key' barplots of... 
    ...on the left: A normalized crosstab for relative distributions.
    ...on the right: An absolute crosstab for a sanity check.
    Args:
        df (DataFrame): Data
        plotcol: Name of column for which the frequency distribution shall be plotted
        refcol: Name of column by which to group. Must be binary with [0, 1].
        show (refcol value, optional): If given, the left plot will only plot 
            the given values. Defaults to None.
        save_as (False or String): If not False, save image with given path
    Returns: None
    '''
    fig, ax = plt.subplots(figsize=(16,3), ncols=2)
    
    # Relative distribution
    crosstab_rel = pd.crosstab(index=df[plotcol], columns=df[refcol], normalize='index')
    if show:
        key = show
    else:
        key = crosstab_rel.columns
    crosstab_rel[key].plot(kind='bar', ax=ax[0], color=['orange'])
    ax[0].set_title(f'Relative frequencies of {refcol} in {plotcol}')
    ax[0].axhline(df[refcol].mean(), color="darkred", linestyle='--')
    
    # Absolute distribution
    crosstab_abs = pd.crosstab(index=df[plotcol], columns="count")
    crosstab_abs.plot(kind='bar', ax=ax[1])
    ax[1].set_title(f'Absolute frequencies of {plotcol}')
    
    if save_as: fig.savefig(save_as)



def value_distribution_plots(df, plotcol, refcol, density=False, save_as=None):
    '''Plot a histogram, boxplot and kernel density estimation (kde) plot, 
        grouped by 'refcol'
    ARGS
        df (DataFrame): Data
        plotcol: Name of value column
        refcol: Name of column by which to group
        density (boolean, optional): If True, the histogram will show 
            density values. Defaults to False.
        save_as (False or String): If not False, save image with given path
    RETURN: None
    '''
    fig, ax = plt.subplots(ncols=3, figsize=(16,3))
    sns.boxplot(data=df, y=plotcol, x=refcol, ax=ax[0])
    df.groupby(refcol)[plotcol].plot(kind='hist', bins=20, ax=ax[1], 
                                       alpha=0.5, density=density)
    df.groupby(refcol)[plotcol].plot(kind='kde', ax=ax[2])
    
    if save_as: fig.savefig(save_as)
