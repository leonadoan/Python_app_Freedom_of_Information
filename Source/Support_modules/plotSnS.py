# To visualise Stop and search class
# By Le Doan 14/01/2021


from stop_search_class import Stop_search_month
from stop_search_class import Stop_search_range
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

""" plot function for Stop and Search in a period """


# Number of case in a period plot
def plotSnS(start_year, start_month, end_year, end_month, area, frame):
    result = Stop_search_range(
                              start_year, start_month,
                              end_year, end_month, area.lower())
    data = result.total_stop_month()
    names = list(data.keys())
    values = list(data.values())

    # Graph the total_stop_by_month
    fig, ax = plt.subplots(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nsew')
    plt.xlabel('Date')
    plt.ylabel('Number of case')

    ax.bar(names, values)
    plt.xticks(rotation='vertical')
    ax.set_title(
                 'Stop and search from ' + start_month + ' ' + start_year
                 + ' to ' + end_month + ' ' + end_year + '\n for ' + area)
    fig.tight_layout()
    plt.show()


""" plot functions for Stop and Search by month """


# Age query plot
def plot_age(year, month, area, frame):
    result = Stop_search_month(year, month, area.lower())
    counts = result.count_age_group()

    # Graph pie chart by age group in a given month
    fig, ax = plt.subplots(figsize=(9, 5), subplot_kw=dict(aspect='equal'))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nsew')

    data = list(counts.values())
    label = counts.keys()

    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(
                                     data, autopct=lambda pct: func(pct, data),
                                     textprops=dict(color='w'))
    ax.legend(
             wedges, label,
             title='Age group',
             loc='center left',
             bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=12, weight='bold')
    ax.set_title(
                  'Pie chart stop search by age in '
                  + area + ' in ' + month + '-' + year)
    fig.tight_layout()
    plt.show()


# Gender query plot


def plot_gender(year, month, area, frame):
    result = Stop_search_month(year, month, area.lower())
    data = result.gender_group()
    names = list(data.keys())
    values = list(data.values())

    # Graph bar chart by gender group in a given month
    fig, ax = plt.subplots(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nsew')
    plt.xlabel('Gender')
    plt.ylabel('Number of case')

    ax.bar(names, values)
    plt.title('Stop search by gender in ' + area + ' in ' + month + '-' + year)
    fig.tight_layout()
    plt.show()

# Ethnicity query plot


def plot_ethnic(year, month, area, frame):
    result = Stop_search_month(year, month, area.lower())
    data = result.ethnic_group()
    names = list(data.keys())
    values = list(data.values())

    names = [name.replace('-', '-\n') for name in names]

    # Graph bar chart by gender group in a given month
    fig, ax = plt.subplots(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nsew')
    plt.xlabel('Number of case')
    plt.ylabel('Ethnicity')

    my_colors = [
                'red', 'blue', 'yellow', 'green', 'coral',
                'pink', 'violet', 'orange', 'grey', 'gold'
                ]
    ax.barh(names, values, color=my_colors)
    plt.title('Stop search by ethnic group in ' + area
              + ' in ' + month + '-' + year)

    fig.tight_layout()
    plt.show()

# Stop search purpose query plot:


def plot_search_object(year, month, area, frame):
    result = Stop_search_month(year, month, area.lower())
    counts = result.object_of_search()

    # Graph pie chart by stop purpose group in a given month
    fig, ax = plt.subplots(figsize=(9, 5), subplot_kw=dict(aspect='equal'))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nsew')
    data = list(counts.values())
    label = list(counts.keys())

    wedges, texts, autotexts = ax.pie(
                                    data, autopct='%1.1f%%',
                                    textprops=dict(color='black'),
                                    pctdistance=1.17)
    ax.legend(
            wedges, label,
            title='Stop Purposes',
            loc='center left',
            bbox_to_anchor=(1, 0, 0, 0))

    plt.setp(autotexts, size=11, weight='bold')
    ax.set_title(
                 'Pie chart stop search purpose in '
                 + area + ' in ' + month + '-' + year)
    fig.tight_layout()
    plt.show()

# Result outcome query plot:


def plot_outcome(year, month, area, frame):
    result = Stop_search_month(year, month, area.lower())
    counts = result.outcome()

    # Graph pie chart by stop outcome group in a given month
    fig, ax = plt.subplots(figsize=(9, 5), subplot_kw=dict(aspect='equal'))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nsew')

    data = list(counts.values())
    label = counts.keys()

    wedges, texts, autotexts = ax.pie(
                                    data, autopct='%1.1f%%',
                                    textprops=dict(color='w'))

    ax.legend(
            wedges, label,
            title='Stop search outcomes',
            loc='center left',
            bbox_to_anchor=(1, 0, 0.5, 0.5))

    plt.setp(autotexts, size=11, weight='bold')
    ax.set_title(
                 'Pie chart stop search outcome in '
                 + area + ' in ' + month + '-' + year)
    fig.tight_layout()
    plt.show()
