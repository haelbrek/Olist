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
