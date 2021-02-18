# To check end-user input value error of Covid app
# By Le Doan 05/01/2021


import tkinter as tk
import Covid_DropBoxOption  # pylint: disable=F0401
import app_function  # pylint: disable=F0401
import datetime as dt

# Area options:
area_list = Covid_DropBoxOption.area_list

# Date limit range for the dataset
upper_limit = dt.datetime(2020, 11, 1)
lower_limit = dt.datetime(2020, 1, 30)


def check_value1(
                start_year, start_month, start_day,
                end_year, end_month, end_day, area):
    check_count = 0

    # Add 0 before if user inputs 1 digit number
    start_month = app_function.add_0(start_month)
    end_month = app_function.add_0(end_month)
    start_day = app_function.add_0(start_day)
    end_day = app_function.add_0(end_day)

    # Check if user inputs a number:
    if app_function.check_num(start_year, start_month, start_day,
                              end_year, end_month, end_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Wrong format! '
                                  + 'Please input a number')
        check_count = 1

    # Check wrong format of all entry boxes:
    elif app_function.check_len_year(start_year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start year must be '
                                  + 'a four-digit number ')
        check_count = 1

    elif app_function.check_len_year(end_year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End year must be '
                                  + 'a four-digit number ')
        check_count = 1

    elif app_function.check_month_value(start_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start month must be '
                                  + 'a two-digit number between 01 and 12')
        check_count = 1

    elif app_function.check_month_value(end_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End month must be '
                                  + 'a two-digit number between 01 and 12')
        check_count = 1

    elif app_function.check_day_value(start_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start day must be '
                                  + 'a two-digit number between 01 and 31')
        check_count = 1

    elif app_function.check_day_value(end_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End day must be '
                                  + 'a two-digit number between 01 and 31')

    elif app_function.check_area(area, area_list) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Your choice of area is'
                                  + ' not in the database '
                                  + '. Please choose an available option in '
                                  + 'the area menu')
        check_count = 1

    if check_count == 0:

        # Check invalid date (number of day in a month)
        if app_function.check_numDayinMonth(start_year,
                                            start_month, start_day) is False \
            or app_function.check_numDayinMonth(end_year,
                                                end_month, end_day) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='You have chosen '
                                      + 'an invalid date.'
                                      + ' Your chosen month does not '
                                      + 'have your chosen day')
            check_count = 1

    # Check input date before 30/01/2020 or after 01/11/2020
    if check_count == 0:
        if app_function.check_date_limit(start_year, start_month, start_day,
                                         end_year, end_month, end_day,
                                         upper_limit, lower_limit) is False:
            tk.messagebox.showwarning(
                                        title='Warning',
                                        message='We only have '
                                        + 'the data from 30/01/2020 '
                                        + 'to 01/11/2020')
            check_count = 1

        # Check start date before or after end date
        elif app_function.check_date_order(start_year, start_month,
                                           start_day, end_year,
                                           end_month, end_day) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='Start date must be '
                                      + 'before the End date')
            check_count = 1

    # Check if the chosen area has the data for the chosen period
    if check_count == 0:
        if app_function.Covid_checkData_area(area, end_year,
                                             end_month, end_day) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='Your chosen area does not '
                                      + 'have data for this chosen period')
            check_count = 1

        return check_count


""" Check value 2 area """


def check_value2(
                start_year, start_month, start_day,
                end_year, end_month, end_day, area1, area2):
    check_count = 0

    # Add 0 before if user inputs 1 digit number
    start_month = app_function.add_0(start_month)
    end_month = app_function.add_0(end_month)
    start_day = app_function.add_0(start_day)
    end_day = app_function.add_0(end_day)

    # Check if user inputs number:
    if app_function.check_num(start_year, start_month, start_day,
                              end_year, end_month, end_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Wrong format! '
                                  + 'Please input a number')
        check_count = 1

    # Check wrong value of all entry boxes:
    elif app_function.check_len_year(start_year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start year must be '
                                  + 'a four-digit number ')
        check_count = 1

    elif app_function.check_len_year(end_year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End year must be '
                                  + 'a four-digit number ')
        check_count = 1

    elif app_function.check_month_value(start_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start month must be '
                                  + 'a two-digit number between 01 and 12')
        check_count = 1

    elif app_function.check_month_value(end_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End month must be '
                                  + 'a two-digit number between 01 and 12')
        check_count = 1

    elif app_function.check_day_value(start_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start day must be '
                                  + 'a two-digit number between 01 and 31')
        check_count = 1

    elif app_function.check_day_value(end_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End day must be a two-digit number '
                                  + 'between 01 and 31')
        check_count = 1

    elif app_function.check_area(area1, area_list) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Your choice of Area 1 '
                                  + 'is not in the database '
                                  + '. Please choose an available option in '
                                  + 'the area menu')
        check_count = 1

    elif app_function.check_area(area2, area_list) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Your choice of Area 2 '
                                  + 'is not in the database '
                                  + '. Please choose an available option in '
                                  + 'the area menu')
        check_count = 1

    if check_count == 0:

        # Check invalid date (number of day in a month)
        if app_function.check_numDayinMonth(start_year,
                                            start_month, start_day) is False \
            or app_function.check_numDayinMonth(end_year,
                                                end_month, end_day) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='You have chosen '
                                      + 'an invalid date.'
                                      + ' Your chosen month does not '
                                      + 'have your chosen day')
            check_count = 1

    # Check input date before 30/01/2020 or after 01/11/2020
    if check_count == 0:
        if app_function.check_date_limit(start_year, start_month, start_day,
                                         end_year, end_month, end_day,
                                         upper_limit, lower_limit) is False:
            tk.messagebox.showwarning(
                                        title='Warning',
                                        message='We only have '
                                        + 'the data from 30/01/2020 '
                                        + 'to 01/11/2020')
            check_count = 1

        # Check start date before or after end date
        elif app_function.check_date_order(start_year, start_month,
                                           start_day, end_year,
                                           end_month, end_day) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='Start date must be '
                                      + 'before the End date')
            check_count = 1

    # Check if the chosen areas has the data for the chosen period
    if check_count == 0:
        if app_function.Covid_checkData_area(area1, end_year,
                                             end_month, end_day) is False:
            tk.messagebox.showwarning(
                                     title='Warning',
                                     message='Your chosen area 1 does not '
                                     + 'have data for this chosen period')
            check_count = 1
        elif app_function.Covid_checkData_area(area2, end_year,
                                               end_month, end_day) is False:
            tk.messagebox.showwarning(
                                     title='Warning',
                                     message='Your chosen area 2 does not '
                                     + 'have data for this chosen period')
            check_count = 1
        return check_count


""" check with no area """


def check_value3(
                start_year, start_month, start_day,
                end_year, end_month, end_day):
    check_count = 0

    # Add 0 before if user inputs 1 digit number
    start_month = app_function.add_0(start_month)
    end_month = app_function.add_0(end_month)
    start_day = app_function.add_0(start_day)
    end_day = app_function.add_0(end_day)

    # Check if user inputs number:
    if app_function.check_num(start_year, start_month, start_day,
                              end_year, end_month, end_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Wrong format! '
                                  + 'Please input a number')
        check_count = 1

    # Check wrong value of all entry boxes:
    elif app_function.check_len_year(start_year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start year must be '
                                  + 'a four-digit number ')
        check_count = 1

    elif app_function.check_len_year(end_year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End year must be '
                                  + 'a four-digit number ')
        check_count = 1

    elif app_function.check_month_value(start_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start month must be '
                                  + 'a two-digit number between 01 and 12')
        check_count = 1

    elif app_function.check_month_value(end_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End month must be '
                                  + 'a two-digit number between 01 and 12')
        check_count = 1

    elif app_function.check_day_value(start_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start day must be '
                                  + 'a two-digit number between 01 and 31')
        check_count = 1

    elif app_function.check_day_value(end_day) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End day must be a two-digit number '
                                  + 'between 01 and 31')
        check_count = 1

    if check_count == 0:
        # Check invalid date (number of day in a month)
        if app_function.check_numDayinMonth(start_year,
                                            start_month, start_day) is False \
            or app_function.check_numDayinMonth(end_year,
                                                end_month, end_day) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='You have chosen '
                                      + 'an invalid date.'
                                      + ' Your chosen month does not '
                                      + 'have your chosen day')
            check_count = 1

    # Check input date before 30/01/2020 or after 01/11/2020
    if check_count == 0:
        if app_function.check_date_limit(start_year, start_month, start_day,
                                         end_year, end_month, end_day,
                                         upper_limit, lower_limit) is False:
            tk.messagebox.showwarning(
                                        title='Warning',
                                        message='We only have '
                                        + 'the data from 30/01/2020 '
                                        + 'to 01/11/2020')
            check_count = 1

        # Check start date before or after end date
        elif app_function.check_date_order(start_year, start_month,
                                           start_day, end_year,
                                           end_month, end_day) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='Start date must be '
                                      + 'before the End date')
            check_count = 1

        return check_count
