# Produce multiple visualization of covid confirmed cases data
# Le Doan 25/11/2020

# Load packages
import pandas as pd
import numpy as np
import os


# Get current file path for data csv file:
currentDir = os.getcwd()
if os.path.isfile('covid_class.py'):  # pragma: no cover
    currentDir = os.path.dirname(currentDir)
dataFolder = "Data"
csvFile = "specimenDate_ageDemographic-unstacked.csv"

dataPath = os.path.join(currentDir, dataFolder, csvFile)
# print(dataPath)

# Load data from csv
data = pd.read_csv(dataPath, parse_dates=['date'])

# Delete unused cols - rolling rate, rolling sum,..
data = data.iloc[:, :26]

# Rename cols:
data = data.rename(columns=lambda s: s.split('-')[1] if '-' in s else s)

# Create a total new confirmed case
data['total_new_case'] = data['0_59'] + data['60+']


""" Create Covid class for an area in a given period """


class Covid:
    area = ''
    start_year = ''
    start_month = ''
    start_day = ''
    end_year = ''
    end_month = ''
    end_day = ''

    def __init__(self, start_year, start_month, start_day,
                 end_year, end_month, end_day, area):
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.end_year = end_year
        self.end_month = end_month
        self.end_day = end_day
        self.area = area

    # Get area name:
    def get_area_name(self):
        return self.area

    # Merge input start date as the date format in data frame
    def start_date_merge(self):
        return self.start_year + '-' + self.start_month + '-' + self.start_day

    # Merge end date as the date format in data frame
    def end_date_merge(self):
        return self.end_year + '-' + self.end_month + '-' + self.end_day

    # Extract covid data for an area in the given period
    def covid_area(self):
        # Extract data within the input are:
        self.df_query = data[data.areaName == self.area]

        # Group data by areaType to avoid
        # the duplicated cases between ltal utla
        by_area_type = self.df_query.groupby('areaType')
        df_by_type = []
        for area, frame in by_area_type:
            df_by_type.append(frame)

        # Get df_query by chosen the first area type:
        self.df_query = df_by_type[0]

        # Extract data between start date and end date
        after_start_date = self.df_query['date'] >= self.start_date_merge()
        before_end_date = self.df_query['date'] <= self.end_date_merge()
        between_two_dates = after_start_date & before_end_date
        self.df_query = self.df_query.loc[between_two_dates]

        return self.df_query

    # Calculate daily infection rate:
    def infection_rate(self):
        filtered_dates = self.covid_area()
        temp = []
        rate = []

        for index, row in filtered_dates.iterrows():
            temp.append(row['total_new_case'])
        for i in range(len(temp)):
            if i == 0:
                rate.append(0)
            elif temp[i-1] != 0:
                rate.append(round((temp[i]-temp[i-1])/temp[i-1] * 100, 2))
            elif temp[i] == 0:
                rate.append(0)
            else:
                rate.append(round((temp[i]-temp[i-1])/(temp[i-1]+1) * 100, 2))

        filtered_dates['rate'] = rate
        return filtered_dates

    # Calculate the rolling 7-day average:
    def moving7avg(self):
        filtered_dates = self.covid_area()
        for i in range(0, filtered_dates.shape[0]-6):
            temp = np.round(((filtered_dates.iloc[i, 26]
                              + filtered_dates.iloc[i+1, 26]
                              + filtered_dates.iloc[i+2, 26]
                              + filtered_dates.iloc[i+3, 26]
                              + filtered_dates.iloc[i+4, 26]
                              + filtered_dates.iloc[i+5, 26]
                              + filtered_dates.iloc[i+6, 26])/7), 1)
            filtered_dates.loc[filtered_dates.index[i+6], 'SMA_7'] = temp
        return filtered_dates

    # Calculate cumulative cases:
    def cumsum_area(self):
        filtered_dates = self.moving7avg()
        temp = filtered_dates.groupby('areaName')['total_new_case'].cumsum()
        filtered_dates['cumulative'] = temp
        return filtered_dates

    # Extract Covid case by 5-band age groups:
    def by_age_groups(self):
        filtered_dates = self.covid_area()
        # Remove unused column such as: areaType, areaCode, Name, date
        df = filtered_dates.iloc[:, 4:26]
        # Drop sub-total age column:
        df = df.drop(columns=['0_59', '60+'])
        # Move column in an order of age:
        x = ['0_4', '5_9']
        cols = x + [col for col in df if col not in x]
        df = df[cols]
        return df


""" Create Covid_info class in a given period """


class Covid_info:
    start_year = ''
    start_month = ''
    start_day = ''
    end_year = ''
    end_month = ''
    end_day = ''

    def __init__(self, start_year, start_month, start_day,
                 end_year, end_month, end_day):
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.end_year = end_year
        self.end_month = end_month
        self.end_day = end_day

    # Merge input start date as the date format in data frame
    def start_date_merge(self):
        return self.start_year + '-' + self.start_month + '-' + self.start_day

    # Merge input end date as the date format in data frame
    def end_date_merge(self):
        return self.end_year + '-' + self.end_month + '-' + self.end_day

    # Extract covid case in a given period:
    def covid_extract(self):
        after_start_date = data['date'] >= self.start_date_merge()
        before_end_date = data['date'] <= self.end_date_merge()
        between_two_dates = after_start_date & before_end_date
        self.df_query = data.loc[between_two_dates]
        return self.df_query

    # Summary covid cases in the UK in a given period:
    def covid_UK(self):
        df_query = self.covid_extract()
        df = df_query[df_query.areaType == 'nation']
        return df

    # Summary covid cases by region in a given period:
    def covid_region(self):
        df_query = self.covid_extract()
        df = df_query[df_query.areaType == 'region']
        temp = df.groupby('areaName')['total_new_case']
        return temp.sum().sort_values(ascending=False)

    # Summary top 5 covid cases by area type - utla in a given period:
    def covid_utla(self):
        df_query = self.covid_extract()
        df = df_query[df_query.areaType == 'utla']
        temp = df.groupby('areaName')['total_new_case']
        return temp.sum().sort_values(ascending=False).head(5)

    # Summary top 5 covid cases by area type - ltla in a given period:
    def covid_ltla(self):
        df_query = self.covid_extract()
        df = df_query[df_query.areaType == 'ltla']
        temp = df.groupby('areaName')['total_new_case']
        return temp.sum().sort_values(ascending=False).head(5)


# Main program:
if __name__ == "__main__":  # pragma: no cover
    x = Covid('2020', '03', '16', '2020', '03', '31', 'Hartlepool')
    print(x.covid_area())
    # print(x.cumsum_area())
    # print(x.moving7avg().iloc[8]['SMA_7'])
    # print(x.infection_rate()['rate'])

    # y = Covid_info('2020', '03', '01', '2020', '03', '01')
