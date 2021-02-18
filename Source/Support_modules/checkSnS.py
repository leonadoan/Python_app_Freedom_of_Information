# To check end-user input value error of Stop & Search app
# By Le Doan 05/01/2021

import datetime as dt
import tkinter as tk
import StopAndSearch_DropBoxOption  # pylint: disable=F0401
import app_function  # pylint: disable=F0401

# Police force options:
police_force_list = StopAndSearch_DropBoxOption.police_force_list

# Date limit range for the dataset
# It is noticed that the API time period covered can be changed overtime
# Therefore, you should check the current limit range
# https://data.police.uk/about/#stop-search
upper_limit = dt.datetime(2020, 11, 1)
lower_limit = dt.datetime(2017, 12, 1)


# Check function to make sure month, year, police force in right format


def check_value1(start_year, start_month, end_year, end_month, area):
    check_count = 0

    # Add 0 before number if user inputs one digit number
    start_month = app_function.add_0(start_month)
    end_month = app_function.add_0(end_month)

    # Check if user inputs number:
    if app_function.check_num(start_year, start_month,
                              end_year, end_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Wrong format! '
                                  + 'Please input a number')
        check_count = 1

    elif app_function.check_len_year(start_year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start year must be '
                                  + 'a four-digit number')
        check_count = 1

    elif app_function.check_len_year(end_year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End year must be '
                                  + 'a four-digit number')
        check_count = 1

    elif app_function.check_month_value(start_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Start month must be a'
                                  + ' two-digit number between 01 and 12')
        check_count = 1

    elif app_function.check_month_value(end_month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='End month must be a '
                                  + 'two-digit number between 01 and 12')
        check_count = 1

    elif app_function.check_area(area, police_force_list) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Your choice of police force '
                                  + 'is not in the database '
                                  + '. Please choose an available option in '
                                  + 'the police force menu')
        check_count = 1

    if check_count == 0:

        # Check start date before or after end date
        if app_function.check_date_order(start_year, start_month, 1,
                                         end_year, end_month, 1) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='Start date must be'
                                      + ' before the End date')
            check_count = 1
        elif app_function.check_date_limit(start_year, start_month, 1,
                                           end_year, end_month, 1,
                                           upper_limit, lower_limit) is False:
            tk.messagebox.showwarning(
                                      title='Warning',
                                      message='We only have '
                                      + 'the data from 12/2017 '
                                      + 'to 11/2020')
            check_count = 1

        return check_count


# Check function to make sure year, month, police force are in the right format


def check_value2(year, month, area):
    check_count = 0

    # Add 0 before number if user inputs one digit number
    month = app_function.add_0(month)

    # Check if user inputs number:
    if app_function.check_num(month, year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Please input a valid number')
        check_count = 1

    elif app_function.check_len_year(year) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Year must be a four-digit number ')
        check_count = 1

    elif app_function.check_month_value(month) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Month must be a two digit number '
                                  + 'between 01 and 12')
        check_count = 1

    elif app_function.check_area(area, police_force_list) is False:
        tk.messagebox.showwarning(
                                  title='Warning',
                                  message='Your choice of police force '
                                  + 'is not in the database. '
                                  + 'Please choose an available option of '
                                  + 'the police force in menu')
        check_count = 1

    if check_count == 0:
        if app_function.check_date_limit(year, month, 1, year, month, 1,
                                         upper_limit, lower_limit) is False:
            tk.messagebox.showwarning(
                                     title='Warning',
                                     message='We only have '
                                     + 'the data from 12/2017 '
                                     + 'to 11/2020')
            check_count = 1

        return check_count
