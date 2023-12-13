import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    df = pd.read_csv("C:/Users/39388/Downloads/fcc-forum-pageviews.csv", index_col='date', parse_dates=True)
    df = df[(df['value'] >= df['value'].quantile(0.025)) &
            (df['value'] <= df['value'].quantile(0.975))]
    
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save and show the plot
    plt.savefig('line_plot.png')
    plt.show()


def draw_bar_plot():
    df = pd.read_csv("C:/Users/39388/Downloads/fcc-forum-pageviews.csv", index_col='date', parse_dates=True)
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%B')  # Converte il formato del mese in testo completo
    
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig, ax = plt.subplots(figsize=(10, 7))
    df_bar.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    plt.xticks(rotation=90)
    
    # Save and show the plot
    plt.savefig('bar_plot.png')
    plt.show()




def draw_box_plot():
    df = pd.read_csv("C:/Users/39388/Downloads/fcc-forum-pageviews.csv", index_col='date', parse_dates=True)
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    
    df_box_year = df.groupby('year')['value'].mean()
    df_box_month = df.groupby(['month', 'year'])['value'].mean().unstack()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    df_box_month = df_box_month.reindex(months)
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))
    sns.boxplot(x=df['year'], y=df['value'], ax=ax[0])
    sns.boxplot(x=df['month'], y=df['value'], ax=ax[1], order=months)
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=90)
    
    # Save and show the plot
    plt.savefig('box_plot.png')
    plt.show()

# Run the functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()
