# To visualise Covid class
# By Le Doan 14/01/2021

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from covid_class import Covid
from covid_class import Covid_info
import numpy as np

""" Plot fuction for Daily and Cumulative number of case of an area """


# Daily case query plot
def plotCovid_10(
                start_year, start_month, start_day,
                end_year, end_month, end_day, area, frame):
    query = Covid(
                  start_year, start_month, start_day,
                  end_year, end_month, end_day, area)
    filtered_dates = query.cumsum_area()
    start_d = query.start_date_merge()
    end_d = query.end_date_merge()

    fig = plt.figure(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    fig.suptitle(
                 'Covid cases in ' + area +
                 ' in the period from ' + start_d + ' to ' + end_d)

    ax1.bar(
            filtered_dates['date'].dt.date,
            filtered_dates['total_new_case'], label='daily case')
    ax1.plot(
             filtered_dates['date'].dt.date,
             filtered_dates['SMA_7'], color='red',
             label='7-day average', linewidth=3)
    ax1.tick_params(axis='x', labelrotation=90)
    ax1.legend()
    ax1.set_ylabel('Number of cases')

    ax2.bar(
            filtered_dates['date'].dt.date,
            filtered_dates['cumulative'], label='cumulative case')
    ax2.tick_params(axis='x', labelrotation=90)
    ax2.legend()
    ax2.set_ylabel('Number of cases')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


# Infection rate query plot


def plotCovid_11(start_year, start_month, start_day,
                 end_year, end_month, end_day, area, frame):
    query = Covid(
                  start_year, start_month, start_day,
                  end_year, end_month, end_day, area)
    filtered_dates = query.infection_rate()
    start_d = query.start_date_merge()
    end_d = query.end_date_merge()

    fig = plt.figure(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
    plt.plot(filtered_dates['date'].dt.date,
             filtered_dates['rate'], linestyle='-',
             marker='o', label='Infection rate')

    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel('Percentage')
    plt.title('Covid infection rates in ' + area +
              ' in the period from ' + start_d + ' to ' + end_d)
    plt.legend()
    fig.tight_layout()
    plt.show()


""" Plot functions for compare between two areas """


# Compare Daily Case plot


def plotCovid_20(
                start_year, start_month, start_day,
                end_year, end_month, end_day, area_1, area_2, frame):
    query1 = Covid(
                  start_year, start_month, start_day,
                  end_year, end_month, end_day, area_1)
    query2 = Covid(
                  start_year, start_month, start_day,
                  end_year, end_month, end_day, area_2)
    dfArea1 = query1.covid_area()
    dfArea2 = query2.covid_area()
    start_date = query1.start_date_merge()
    end_date = query1.end_date_merge()

    fig = plt.figure(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
    plt.plot(
            dfArea1['date'].dt.date, dfArea1['total_new_case'],
            color='blue', label=dfArea1.iloc[0]['areaName'])
    plt.plot(
            dfArea2['date'].dt.date, dfArea2['total_new_case'],
            color='red', label=dfArea2.iloc[0]['areaName'])
    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel('Number of cases')
    plt.title(
             'Areas comparison in the period from '
             + start_date + ' to ' + end_date)
    plt.legend()
    fig.tight_layout()
    plt.show()

# Compare by age group plot


def plotCovid_21(
              start_year, start_month, start_day,
              end_year, end_month, end_day, area_1, area_2, frame):
    query1 = Covid(
                   start_year, start_month, start_day,
                   end_year, end_month, end_day, area_1)
    query2 = Covid(
                   start_year, start_month, start_day,
                   end_year, end_month, end_day, area_2)
    dfArea1 = query1.by_age_groups()
    dfArea2 = query2.by_age_groups()
    start_date = query1.start_date_merge()
    end_date = query1.end_date_merge()

    width = 0.45  # the width of the bars

    fig = plt.figure(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
    a = np.arange(len(list(dfArea1)))
    plt.bar(a - width/2, dfArea1.sum(), width, label=area_1)
    plt.bar(a + width/2, dfArea2.sum(), width, label=area_2)
    plt.xticks(a, list(dfArea1), rotation=90)
    plt.xlabel('Age groups')
    plt.ylabel('Number of cases')
    plt.title(
              'Areas comparison by age groups in the period from '
              + start_date + ' to ' + end_date)
    plt.legend()
    fig.tight_layout()
    plt.show()


""" plot function for Covid general information for a given period """


# Region query plot
def plotCovid_30(
                start_year, start_month, start_day,
                end_year, end_month, end_day, frame):
    query = Covid_info(
                      start_year, start_month, start_day,
                      end_year, end_month, end_day)

    input = query.covid_region()

    temp = dict(input)
    values = temp.values()
    labels = temp.keys()

    start_date = query.start_date_merge()
    end_date = query.end_date_merge()

    fig = plt.figure(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')

    plt.bar(labels, values, color='blue')
    plt.xlabel('Region')
    plt.ylabel('Number of cases')
    plt.title(
              'Covid cases by region in the period from '
              + start_date + ' to ' + end_date)

    plt.xticks(rotation=45, ha='right', fontsize=9)
    fig.tight_layout()
    plt.show()


# Top 5 UTLA query plot


def plotCovid_31(
                start_year, start_month, start_day,
                end_year, end_month, end_day, frame):
    query = Covid_info(start_year, start_month, start_day,
                       end_year, end_month, end_day)

    input = query.covid_utla()

    temp = dict(input)
    values = temp.values()
    labels = temp.keys()

    start_date = query.start_date_merge()
    end_date = query.end_date_merge()

    fig = plt.figure(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')

    plt.bar(labels, values, color='blue')
    plt.xlabel('Utla areas')
    plt.ylabel('Number of cases')
    plt.title(
              'Top 5 Covid cases by Utla areas in the period from '
              + start_date + ' to ' + end_date)

    # plt.xticks(rotation=90)
    fig.tight_layout()
    plt.show()


# Top 5 ITLA query plot


def plotCovid_32(
                start_year, start_month, start_day,
                end_year, end_month, end_day, frame):
    query = Covid_info(start_year, start_month, start_day,
                       end_year, end_month, end_day)

    input = query.covid_ltla()

    temp = dict(input)
    values = temp.values()
    labels = temp.keys()

    start_date = query.start_date_merge()
    end_date = query.end_date_merge()

    fig = plt.figure(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')

    plt.bar(labels, values, color='blue')
    plt.xlabel('ltla areas')
    plt.ylabel('Number of cases')
    plt.title(
              'Top 5 Covid cases by ltla areas in the period from '
              + start_date + ' to ' + end_date)

    # plt.xticks(rotation=90)
    fig.tight_layout()
    plt.show()

# Daily case in the UK plot


def plotCovid_33(
                start_year, start_month, start_day,
                end_year, end_month, end_day, frame):
    query = Covid_info(start_year, start_month, start_day,
                       end_year, end_month, end_day)
    df = query.covid_UK()
    start_date = query.start_date_merge()
    end_date = query.end_date_merge()

    fig = plt.figure(figsize=(9, 5))
    chart = FigureCanvasTkAgg(fig, frame)
    chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
    plt.bar(
             df['date'].dt.date, df['total_new_case'],
             color='blue')

    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel('Number of cases')
    plt.title(
              'Daily Covid cases in the UK '
              + start_date + ' to ' + end_date)

    fig.tight_layout()
    plt.show()
