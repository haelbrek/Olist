import seaborn as sns
import matplotlib.pyplot as plt

ax = plt.subplots()

def counts_in_percentages(column):
    counts =  column.value_counts()
    return counts/counts.sum()*100



import pandas as pd

def difference_in_time(df, date1, date2, new_column_name, time_unit):
    df[date1] = pd.to_datetime(df[date1], format='%Y-%m-%d %H:%M:%S')
    df[date2] = pd.to_datetime(df[date2], format='%Y-%m-%d %H:%M:%S')
    
    if time_unit == 'day':
        df[new_column_name] = (df[date2] - df[date1]).dt.days
    elif time_unit == 'month':
        df[new_column_name] = (df[date2].dt.year - df[date1].dt.year) * 12 + (df[date2].dt.month - df[date1].dt.month)
    elif time_unit == 'year':
        df[new_column_name] = (df[date2].dt.year - df[date1].dt.year)
    elif time_unit == 'week':
        df[new_column_name] = (df[date2] - df[date1]).dt.total_seconds() / (24 * 60 * 60 * 7)
    else:
        print('Invalid time unit. Please choose from day, month, year, or week.')
        return
    
    return df



import matplotlib.pyplot as plt

def plot_two_plots(df, title1, title2, xlabel1, xlabel2, fontsize, rotation):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,4))
    
    df_grouped = df.groupby(df['order_purchase_timestamp'].dt.date).mean()
    ax1.plot(df_grouped.index, df_grouped['diff_in_day'])
    ax1.set_title(title1, fontsize=fontsize)
    ax1.set_xlabel(xlabel1, fontsize=fontsize)
    ax1.set_ylabel('diff_in_day', fontsize=fontsize)
    #ax1.set_xticks(fontsize=fontsize, rotation=rotation)
    #ax1.set_yticks(fontsize=fontsize)

    df_2017 = df[df['order_purchase_timestamp'].dt.year >= 2017]
    df_grouped = df_2017.groupby(df_2017['order_purchase_timestamp'].dt.date).mean()
    ax2.plot(df_grouped.index, df_grouped['diff_in_day'])
    ax2.axhline(y=1, color='red', linestyle='--')
    ax2.set_title(title2, fontsize=fontsize)
    ax2.set_xlabel(xlabel2, fontsize=fontsize)
    ax2.set_ylabel('diff_in_day', fontsize=fontsize)
    #ax2.set_xticks(fontsize=fontsize, rotation=rotation)
    #ax2.set_yticks(fontsize=fontsize)    
    plt.show()