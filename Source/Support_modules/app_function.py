# To build functions supported for the app
# Le Doan 05/01/2021

import datetime as dt
import Covid_DropBoxOption  # pylint: disable=F0401
import covid_class  # pylint: disable=F0401
from calendar import monthrange

# Check function to make sure month, year, police force in right format

month_value = Covid_DropBoxOption.month_value
day_value = Covid_DropBoxOption.day_value


def add_0(input_value):
    flex_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if input_value in flex_value:
        input_value = '0' + input_value
    return input_value


# Check whether the string arguments are numeric


def check_num(*args):
    for i in args:
        if i.isnumeric() is False:
            break
    return i.isnumeric()


# Check whether the len of year is 4 digit


def check_len_year(year):
    if len(year) != 4:
        result = False
    else:
        result = True
    return result


# Check month value from 01 to 12


def check_month_value(month):
    if month not in month_value:
        result = False
    else:
        result = True
    return result

# Check day value from 01 to 31


def check_day_value(day):
    if day not in day_value:
        result = False
    else:
        result = True
    return result


# Check whether the input area is in the area list


def check_area(area, area_list):
    if area not in area_list:
        result = False
    else:
        result = True
    return result


# Check the validity of input day for a month
# i.e. February dose not have 30 days


def check_numDayinMonth(year, month, day):
    (weekDay, numberOfDays) = monthrange(int(year), int(month))
    if int(day) > numberOfDays:
        result = False
    else:
        result = True
    return result


# Check the input date is in data provided date from 30/01/2020 to 01/11/2020


def check_date_limit(start_year, start_month, start_day,
                     end_year, end_month, end_day,
                     upper_limit, lower_limit):

    start_date = dt.datetime(int(start_year), int(start_month), int(start_day))
    end_date = dt.datetime(int(end_year), int(end_month), int(end_day))
    if (start_date < lower_limit) \
            or (start_date > upper_limit) \
            or (end_date > upper_limit) \
            or (end_date < lower_limit):
        result = False
    else:
        result = True
    return result


# Check the order of date i.e. start date is before end date


def check_date_order(start_year, start_month, start_day,
                     end_year, end_month, end_day):

    start_date = dt.datetime(int(start_year), int(start_month), int(start_day))
    end_date = dt.datetime(int(end_year), int(end_month), int(end_day))

    if start_date > end_date:
        result = False
    else:
        result = True
    return result


def Covid_checkData_area(area, y, m, d):
    df_query = covid_class.data[covid_class.data.areaName == area]
    date_df = df_query['date'].min()
    date_query = dt.datetime(int(y), int(m), int(d))

    # Check input date is after the date in data for that area
    if date_df <= date_query:
        result = True
    else:
        result = False
    return result
