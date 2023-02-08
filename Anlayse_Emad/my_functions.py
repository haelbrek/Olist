import seaborn as sns

def counts_in_percentages(column):
    counts =  column.value_counts()
    return counts/counts.sum()



def annotate_barplot(ax, size = 10):
    for p in ax.patches:
        height = p.get_height()
        ax.annotate('{:.2f}%'.format(height),
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='center',
                    xytext=(0, 10), textcoords='offset points',
                    fontsize=size, color='black')

def my_sns_barplot(column, ax_i = 0, ax_j = 0, xlabel = "", ylabel = "", xrotation = 0, yrotation = 0, annotate = False, annotate_size = 10, rotation = 0):
    sns.barplot(x=column.index, y=column.values, ax = ax[ax_i][ax_j])
    ax[ax_i][ax_j].set_xlabel(xlabel)
    ax[ax_i][ax_j].set_xticklabels(ax[ax_i][ax_j].get_xticklabels(), rotation=rotation)
    if annotate == True:
        annotate_barplot(ax[ax_i][ax_j], size=annotate_size)