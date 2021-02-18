# GUI for FOI app
# By Le Doan 14/01/2021

# Import package:
import tkinter as tk
from tkinter import ttk

import sys
sys.path += ['Support_modules']

# Import modules:
# tkentrycomplete is a third party module,
# a dropbox with "try to complete" ability
import tkentrycomplete as tkec  # noqa: E402
# Store Stop and Search box options:
import StopAndSearch_DropBoxOption  # noqa: E402
# Store Covid box options:
import Covid_DropBoxOption  # noqa: E402
# Check input format for Covid:
import checkCovid  # noqa: E402
# Check input format for Stop and Search:
import checkSnS  # noqa: E402
# Plot functions for Stop and Search:
import plotSnS  # noqa: E402
# Plot functions for Covid:
import plotCovid  # noqa: E402, pylint: disable=all


""" Create root class for the main interface for this app """


class root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('1300x650')
        self.title('Freedom of Information')

        Frame = tk.Frame(self)
        Frame.pack(side='top', fill='both', expand=True)
        Frame.grid_rowconfigure(0, weight=1)
        Frame.grid_columnconfigure(0, weight=1)

        # Create a dictionary in frames so each page
        # For the functions can be defined with a class.
        self.frames = {}

        # Represent all of the individual pages
        # and append them to the dictionary
        # F represets frame:
        for F in (
                 StartPage, AppSnS1, AppSnS2,
                 AppCovid1, AppCovid2, AppCovid3):
            frame = F(Frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    # Define the function for showing each frame as their button is clicked
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


""" Create a start page with buttons leading to different types of query"""


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(
                        self, text='Welcome to Freedom of Information App!\n'
                        + 'Please choose a type of query:',
                          borderwidth=5, relief='solid',
                          anchor='c', justify='center',
                          background='blue', foreground='white', font=20)
        label.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

        # Create left, right and center frame
        leftframe = tk.Frame(self, width=300, height=300, bg='light blue')
        leftframe.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        rightframe = tk.Frame(self, width=300, height=300, bg='light blue')
        rightframe.grid(row=1, column=2, sticky='nesw', padx=10, pady=10)

        centerframe = tk.Frame(self, width=400, height=300, bg='yellow')
        centerframe.grid(row=1, column=1, sticky='nesw', padx=10, pady=10)

        # Create Stop and Search menu:
        StartPage.label_1 = tk.Label(
                                    leftframe, text='Stop and Search section:',
                                    borderwidth=3, relief='solid',
                                    anchor='c', justify='center',
                                    background='blue', foreground='white')
        StartPage.label_1.grid(row=0, column=0, sticky='nesw',
                               padx=10, pady=10)

        StartPage.app_1 = ttk.Button(
                                    leftframe, cursor='hand2',
                                    text='Stop and Search in a period',
                                    command=lambda:
                                    controller.show_frame(AppSnS1))
        StartPage.app_1.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        StartPage.app_2 = ttk.Button(
                                    leftframe, cursor='hand2',
                                    text='Stop and Search by month',
                                    command=lambda:
                                    controller.show_frame(AppSnS2))
        StartPage.app_2.grid(row=2, column=0, sticky='nesw', padx=10, pady=10)

        # Create Covid menu:
        StartPage.label_2 = tk.Label(
                                     rightframe,
                                     text='Covid-19 Confirmed Cases section:',
                                     borderwidth=3, relief='solid',
                                     anchor='c', justify='center',
                                     background='blue', foreground='white')
        StartPage.label_2.grid(row=0, column=0, sticky='nesw',
                               padx=10, pady=10)

        StartPage.app_11 = ttk.Button(
                                      rightframe, cursor='hand2',
                                      text='Daily and cumulative number'
                                      + ' of cases of an area',
                                      command=lambda:
                                      controller.show_frame(AppCovid1))
        StartPage.app_11.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        StartPage.app_12 = ttk.Button(
                                      rightframe, cursor='hand2',
                                      text='Compare between two areas',
                                      command=lambda:
                                      controller.show_frame(AppCovid2))
        StartPage.app_12.grid(row=2, column=0, sticky='nesw', padx=10, pady=10)

        StartPage.app_13 = ttk.Button(
                                     rightframe, cursor='hand2',
                                     text='Covid general information'
                                     + ' for a given period',
                                     command=lambda:
                                     controller.show_frame(AppCovid3))
        StartPage.app_13.grid(row=4, column=0, sticky='nesw', padx=10, pady=10)

        StartPage.logo = tk.PhotoImage(file='Data/teesside.png')
        StartPage.img = tk.Label(centerframe, image=StartPage.logo)
        StartPage.img.grid(row=0, column=0, sticky='nesw')

        # quit window button
        self.quit_button = ttk.Button(
                                    self, text="QUIT", cursor='hand2',
                                    command=controller.quit)
        self.quit_button.grid(row=2, column=1, sticky='nesw', padx=10, pady=10)

        signature = tk.Label(
                            self, text='Designed by Le Minh Thao Doan 2020',
                            borderwidth=5, relief='solid',
                            anchor='c', justify='center',
                            background='blue', foreground='white', font=20)
        signature.grid(row=5, column=1, sticky='nesw', padx=10, pady=10)


""" Stop and Search by period"""


class AppSnS1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Call box option value
        month_value = StopAndSearch_DropBoxOption.month_value
        year_value = StopAndSearch_DropBoxOption.year_value
        police_force_list = StopAndSearch_DropBoxOption.police_force_list

        # Create title
        title_label = tk.Label(
                               self, text='Stop and Search for '
                               + ' a period of time\n'
                               + 'Please choose a period '
                               + 'between 12/2017 and 11/2020',
                               font=20, borderwidth=5, relief='solid',
                               anchor='c', justify='center',
                               background='blue', foreground='white')
        title_label.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

        # Create left frame and right frame:
        leftframe = tk.Frame(self, width=200, height=500, bg='grey')
        leftframe.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        rightframe = tk.Frame(self, width=600, height=500, bg='white')
        rightframe.grid(row=1, column=1, sticky='nesw', padx=10, pady=10)

        # Create start month option:
        AppSnS1.start_month = ttk.Label(leftframe,
                                        text='Start month:', font=10)
        AppSnS1.start_month.grid(row=2, column=0,
                                 sticky='nesw', padx=10, pady=10)
        AppSnS1.start_month_entry = tkec.AutocompleteCombobox(leftframe)
        AppSnS1.start_month_entry.set_completion_list(month_value)
        AppSnS1.start_month_entry.grid(row=2, column=1,
                                       sticky='nesw', padx=10, pady=10)
        AppSnS1.start_month_entry.insert(0, '05')

        # Create start year option:
        AppSnS1.start_year = ttk.Label(leftframe, text='Start year:', font=10)
        AppSnS1.start_year.grid(row=3, column=0,
                                sticky='nesw', padx=10, pady=10)
        AppSnS1.start_year_entry = tkec.AutocompleteCombobox(leftframe)
        AppSnS1.start_year_entry.set_completion_list(year_value)
        AppSnS1.start_year_entry.grid(row=3, column=1,
                                      sticky='nesw', padx=10, pady=10)
        AppSnS1.start_year_entry.insert(0, '2020')

        # Create end month option
        AppSnS1.end_month = ttk.Label(leftframe, text='End month:', font=10)
        AppSnS1.end_month.grid(row=4, column=0,
                               sticky='nesw', padx=10, pady=10)
        AppSnS1.end_month_entry = tkec.AutocompleteCombobox(leftframe)
        AppSnS1.end_month_entry.set_completion_list(month_value)
        AppSnS1.end_month_entry.grid(row=4, column=1,
                                     sticky='nesw', padx=10, pady=10)
        AppSnS1.end_month_entry.insert(0, '10')

        # Create end year option
        AppSnS1.end_year = ttk.Label(leftframe, text='End year:', font=10)
        AppSnS1.end_year.grid(row=5, column=0, sticky='nesw', padx=10, pady=10)
        AppSnS1.end_year_entry = tkec.AutocompleteCombobox(leftframe)
        AppSnS1.end_year_entry.set_completion_list(year_value)
        AppSnS1.end_year_entry.grid(row=5, column=1,
                                    sticky='nesw', padx=10, pady=10)
        AppSnS1.end_year_entry.insert(0, '2020')

        # Create police force option
        AppSnS1.police_force = ttk.Label(leftframe,
                                         text='Police force:', font=10)
        AppSnS1.police_force.grid(row=6, column=0,
                                  sticky='nesw', padx=10, pady=10)
        AppSnS1.police_force_entry = tkec.AutocompleteCombobox(leftframe)
        AppSnS1.police_force_entry.set_completion_list(police_force_list)
        AppSnS1.police_force_entry.grid(row=6, column=1,
                                        sticky='nesw', padx=10, pady=10)
        AppSnS1.police_force_entry.insert(0, 'Cleveland')

        # Create query button
        query_button = ttk.Button(
                                  leftframe, cursor='hand2',
                                  text='Query', command=lambda:
                                  app_run(AppSnS1.start_year_entry.get(),
                                          AppSnS1.start_month_entry.get(),
                                          AppSnS1.end_year_entry.get(),
                                          AppSnS1.end_month_entry.get(),
                                          AppSnS1.police_force_entry.get()))
        query_button.grid(row=7, column=1, sticky='nesw', padx=10, pady=10)

        # Create back button
        back_button = ttk.Button(
                                 leftframe, cursor='hand2', text='Back',
                                 command=lambda:
                                 controller.show_frame(StartPage))
        back_button.grid(row=7, column=0, sticky='nesw', padx=10, pady=10)

        # Create quit button
        quit_button = ttk.Button(
                                 leftframe, cursor='hand2', text="QUIT",
                                 command=controller.quit)
        quit_button.grid(row=8, column=0, sticky='nesw', padx=10, pady=10)

        # Call function to check input format, then plot graph
        def app_run(start_year, start_month, end_year, end_month, area):
            check_count = checkSnS.check_value1(start_year, start_month,
                                                end_year, end_month, area)
            if check_count == 0:
                plotSnS.plotSnS(start_year, start_month, end_year,
                                end_month, area, rightframe)


""" Stop and Search in one month """


class AppSnS2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        month_value = StopAndSearch_DropBoxOption.month_value
        year_value = StopAndSearch_DropBoxOption.year_value
        police_force_list = StopAndSearch_DropBoxOption.police_force_list

        title_label = tk.Label(
                               self, text='Stop and Search by month\n'
                               + 'Please choose a month '
                               + 'between 12/2017 and 11/2020',
                               borderwidth=5, relief='solid', anchor='c',
                               justify='center', font=20,
                               background='blue', foreground='white')
        title_label.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

        # Create left frame and right frame:
        leftframe = tk.Frame(self, width=200, height=500, bg='grey')
        leftframe.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        rightframe = tk.Frame(self, width=600, height=500, bg='white')
        rightframe.grid(row=1, column=1, sticky='nesw', padx=10, pady=10)

        # Create month option:
        AppSnS2.month = ttk.Label(leftframe, text='Month:', font=10)
        AppSnS2.month.grid(row=2, column=0, sticky='nesw', padx=10, pady=10)
        AppSnS2.month_entry = tkec.AutocompleteCombobox(leftframe)
        AppSnS2.month_entry.set_completion_list(month_value)
        AppSnS2.month_entry.grid(row=2, column=1,
                                 sticky='nesw', padx=10, pady=10)
        AppSnS2.month_entry.insert(0, '03')

        # Create start year option:
        AppSnS2.year = ttk.Label(leftframe, text='Year:', font=10)
        AppSnS2.year.grid(row=3, column=0, sticky='nesw', padx=10, pady=10)
        AppSnS2.year_entry = tkec.AutocompleteCombobox(leftframe)
        AppSnS2.year_entry.set_completion_list(year_value)
        AppSnS2.year_entry.grid(row=3, column=1,
                                sticky='nesw', padx=10, pady=10)
        AppSnS2.year_entry.insert(0, '2019')

        # Create police force option:
        AppSnS2.police_force = ttk.Label(leftframe,
                                         text='Police force:', font=10)
        AppSnS2.police_force.grid(row=4, column=0,
                                  sticky='nesw', padx=10, pady=10)
        AppSnS2.police_force_entry = tkec.AutocompleteCombobox(leftframe)
        AppSnS2.police_force_entry.set_completion_list(police_force_list)
        AppSnS2.police_force_entry.grid(row=4, column=1,
                                        sticky='nesw', padx=10, pady=10)
        AppSnS2.police_force_entry.insert(0, 'Cleveland')

        # Create query1 button:
        query1_button = ttk.Button(
                                  leftframe,
                                  cursor='hand2', text='Age Query',
                                  command=lambda: run_app1(
                                      AppSnS2.year_entry.get(),
                                      AppSnS2.month_entry.get(),
                                      AppSnS2.police_force_entry.get()))
        query1_button.grid(row=6, column=1, sticky='nesw', padx=10, pady=10)

        # Create query2 button:
        query2_button = ttk.Button(
                                  leftframe,
                                  cursor='hand2', text='Gender Query',
                                  command=lambda: run_app2(
                                      AppSnS2.year_entry.get(),
                                      AppSnS2.month_entry.get(),
                                      AppSnS2.police_force_entry.get()))
        query2_button.grid(row=7, column=1, sticky='nesw', padx=10, pady=10)

        # Create query3 button:
        query3_button = ttk.Button(
                                  leftframe,
                                  cursor='hand2', text='Ethnic Query',
                                  command=lambda: run_app3(
                                      AppSnS2.year_entry.get(),
                                      AppSnS2.month_entry.get(),
                                      AppSnS2.police_force_entry.get()))
        query3_button.grid(row=8, column=1, sticky='nesw', padx=10, pady=10)

        # Create query4 button:
        query4_button = ttk.Button(
                                  leftframe, cursor='hand2',
                                  text='Stop Purpose Query',
                                  command=lambda: run_app4(
                                      AppSnS2.year_entry.get(),
                                      AppSnS2.month_entry.get(),
                                      AppSnS2.police_force_entry.get()))
        query4_button.grid(row=9, column=1, sticky='nesw', padx=10, pady=10)

        # Create query4 button:
        query5_button = ttk.Button(
                                  leftframe, cursor='hand2',
                                  text='Result Outcome Query',
                                  command=lambda: run_app5(
                                      AppSnS2.year_entry.get(),
                                      AppSnS2.month_entry.get(),
                                      AppSnS2.police_force_entry.get()))
        query5_button.grid(row=10, column=1, sticky='nesw', padx=10, pady=10)

        # Create back button:
        back_button = ttk.Button(
                                 leftframe, cursor='hand2', text='Back',
                                 command=lambda:
                                 controller.show_frame(StartPage))
        back_button.grid(row=6, column=0, sticky='nesw', padx=10, pady=10)

        # Create quit button:
        quit_button = ttk.Button(
                                 leftframe, text='QUIT', cursor='hand2',
                                 command=controller.quit)
        quit_button.grid(row=7, column=0, sticky='nesw', padx=10, pady=10)

        # Check input format and call plot function:
        # Plot function for age query button
        def run_app1(year, month, area):
            check_count = checkSnS.check_value2(year, month, area)
            if check_count == 0:
                plotSnS.plot_age(year, month, area, rightframe)

        # Plot function for gender query button
        def run_app2(year, month, area):
            check_count = checkSnS.check_value2(year, month, area)
            if check_count == 0:
                plotSnS.plot_gender(year, month, area, rightframe)

        # Plot function for ethnic query button
        def run_app3(year, month, area):
            check_count = checkSnS.check_value2(year, month, area)
            if check_count == 0:
                plotSnS.plot_ethnic(year, month, area, rightframe)

        # Plot function for stop purpose button
        def run_app4(year, month, area):
            check_count = checkSnS.check_value2(year, month, area)
            if check_count == 0:
                plotSnS.plot_search_object(year, month, area, rightframe)

        # Plot function for result outcome button
        def run_app5(year, month, area):
            check_count = checkSnS.check_value2(year, month, area)
            if check_count == 0:
                plotSnS.plot_outcome(year, month, area, rightframe)


""" Covid App - Daily and cumulative number of cases of an area
over a given period """


class AppCovid1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        month_value = Covid_DropBoxOption.month_value
        day_value = Covid_DropBoxOption.day_value
        year_value = Covid_DropBoxOption.year_value
        area_list = Covid_DropBoxOption.area_list

        title_label = tk.Label(
                               self, justify='center', font=20,
                               text='Daily and cumulative number of cases '
                               + 'of an area over a given period',
                               borderwidth=5, relief='solid', anchor='c',
                               background='blue', foreground='white')
        title_label.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

        # Create left frame and right frame:
        leftframe = tk.Frame(self, width=200, height=500, bg='grey')
        leftframe.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        rightframe = tk.Frame(self, width=600, height=500, bg='white')
        rightframe.grid(row=1, column=1, sticky='nesw', padx=10, pady=10)

        # Create start day option:
        AppCovid1.start_day = ttk.Label(leftframe, text='Start Day:', font=10)
        AppCovid1.start_day.grid(row=0, column=0,
                                 sticky='nesw', padx=10, pady=10)
        AppCovid1.start_day_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid1.start_day_entry.set_completion_list(day_value)
        AppCovid1.start_day_entry.grid(row=0, column=1,
                                       sticky='nesw', padx=10, pady=10)
        AppCovid1.start_day_entry.insert(0, '01')

        # Create start month option:
        AppCovid1.start_month = ttk.Label(leftframe,
                                          text='Start Month:', font=10)
        AppCovid1.start_month.grid(row=1, column=0,
                                   sticky='nesw', padx=10, pady=10)
        AppCovid1.start_month_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid1.start_month_entry.set_completion_list(month_value)
        AppCovid1.start_month_entry.grid(row=1, column=1,
                                         sticky='nesw', padx=10, pady=10)
        AppCovid1.start_month_entry.insert(0, '04')

        # Create start year option:
        AppCovid1.start_year = ttk.Label(leftframe,
                                         text='Start Year:', font=10)
        AppCovid1.start_year.grid(row=2, column=0,
                                  sticky='nesw', padx=10, pady=10)
        AppCovid1.start_year_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid1.start_year_entry.set_completion_list(year_value)
        AppCovid1.start_year_entry.grid(row=2, column=1,
                                        sticky='nesw', padx=10, pady=10)
        AppCovid1.start_year_entry.insert(0, '2020')

        # Create end day option:
        AppCovid1.end_day = ttk.Label(leftframe, text='End Day:', font=10)
        AppCovid1.end_day.grid(row=3, column=0,
                               sticky='nesw', padx=10, pady=10)
        AppCovid1.end_day_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid1.end_day_entry.set_completion_list(day_value)
        AppCovid1.end_day_entry.grid(row=3, column=1,
                                     sticky='nesw', padx=10, pady=10)
        AppCovid1.end_day_entry.insert(0, '01')

        # Create end month option:
        AppCovid1.end_month = ttk.Label(leftframe, text='End Month:', font=10)
        AppCovid1.end_month.grid(row=4, column=0,
                                 sticky='nesw', padx=10, pady=10)
        AppCovid1.end_month_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid1.end_month_entry.set_completion_list(month_value)
        AppCovid1.end_month_entry.grid(row=4, column=1,
                                       sticky='nesw', padx=10, pady=10)
        AppCovid1.end_month_entry.insert(0, '08')

        # Create end year option:
        AppCovid1.end_year = ttk.Label(leftframe, text='End Year:', font=10)
        AppCovid1.end_year.grid(row=5, column=0,
                                sticky='nesw', padx=10, pady=10)
        AppCovid1.end_year_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid1.end_year_entry.set_completion_list(year_value)
        AppCovid1.end_year_entry.grid(row=5, column=1,
                                      sticky='nesw', padx=10, pady=10)
        AppCovid1.end_year_entry.insert(0, '2020')

        # Create area option:
        AppCovid1.area = ttk.Label(leftframe, text='Area:', font=10)
        AppCovid1.area.grid(row=6, column=0, sticky='nesw', padx=10, pady=10)
        AppCovid1.area_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid1.area_entry.set_completion_list(area_list)
        AppCovid1.area_entry.grid(row=6, column=1,
                                  sticky='nesw', padx=10, pady=10)
        AppCovid1.area_entry.insert(0, 'Hartlepool')

        # Create query button:
        query1_button = ttk.Button(
                                  leftframe,
                                  text='Daily Case Query', cursor='hand2',
                                  command=lambda:
                                  run_app1(AppCovid1.start_year_entry.get(),
                                           AppCovid1.start_month_entry.get(),
                                           AppCovid1.start_day_entry.get(),
                                           AppCovid1.end_year_entry.get(),
                                           AppCovid1.end_month_entry.get(),
                                           AppCovid1.end_day_entry.get(),
                                           AppCovid1.area_entry.get()))
        query1_button.grid(row=7, column=1, sticky='nesw', padx=10, pady=10)

        query2_button = ttk.Button(
                                  leftframe,
                                  text='Infection Rate Query', cursor='hand2',
                                  command=lambda:
                                  run_app2(AppCovid1.start_year_entry.get(),
                                           AppCovid1.start_month_entry.get(),
                                           AppCovid1.start_day_entry.get(),
                                           AppCovid1.end_year_entry.get(),
                                           AppCovid1.end_month_entry.get(),
                                           AppCovid1.end_day_entry.get(),
                                           AppCovid1.area_entry.get()))
        query2_button.grid(row=8, column=1, sticky='nesw', padx=10, pady=10)

        # Create back button
        back_button = ttk.Button(
                                 leftframe, cursor='hand2', text='Back',
                                 command=lambda:
                                 controller.show_frame(StartPage))
        back_button.grid(row=7, column=0, sticky='nesw', padx=10, pady=10)

        # Create quit button
        quit_button = ttk.Button(
                                leftframe, cursor='hand2', text='QUIT',
                                command=controller.quit)
        quit_button.grid(row=8, column=0, sticky='nesw', padx=10, pady=10)

        # Call check format function and Plot daily case
        def run_app1(
                    start_year, start_month, start_day,
                    end_year, end_month, end_day, area):
            check_count = checkCovid.check_value1(
                                      start_year, start_month, start_day,
                                      end_year, end_month, end_day, area)
            if check_count == 0:
                plotCovid.plotCovid_10(
                            start_year, start_month, start_day,
                            end_year, end_month, end_day, area, rightframe)

        # Call check format function and Plot infection rate
        def run_app2(
                    start_year, start_month, start_day,
                    end_year, end_month, end_day, area):
            check_count = checkCovid.check_value1(
                                      start_year, start_month, start_day,
                                      end_year, end_month, end_day, area)
            if check_count == 0:
                plotCovid.plotCovid_11(
                            start_year, start_month, start_day,
                            end_year, end_month, end_day, area, rightframe)


""" Covid App - Compare between two areas """


class AppCovid2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        month_value = Covid_DropBoxOption.month_value
        day_value = Covid_DropBoxOption.day_value
        year_value = Covid_DropBoxOption.year_value
        area_list = Covid_DropBoxOption.area_list

        title_label = tk.Label(
                                self, text='Compare between two areas',
                                borderwidth=5, relief='solid',
                                anchor='c', justify='center', font=20,
                                background='blue', foreground='white')
        title_label.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

        # Create left frame and right frame:
        leftframe = tk.Frame(self, width=200, height=500, bg='grey')
        leftframe.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        rightframe = tk.Frame(self, width=600, height=500, bg='white')
        rightframe.grid(row=1, column=1, sticky='nesw', padx=10, pady=10)

        # Create start day option:
        AppCovid2.start_day = ttk.Label(leftframe, text='Start Day:', font=10)
        AppCovid2.start_day.grid(row=0, column=0,
                                 sticky='nesw', padx=10, pady=10)
        AppCovid2.start_day_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid2.start_day_entry.set_completion_list(day_value)
        AppCovid2.start_day_entry.grid(row=0, column=1,
                                       sticky='nesw', padx=10, pady=10)
        AppCovid2.start_day_entry.insert(0, '01')

        # Create start month option:
        AppCovid2.start_month = ttk.Label(leftframe,
                                          text='Start Month:', font=10)
        AppCovid2.start_month.grid(row=1, column=0,
                                   sticky='nesw', padx=10, pady=10)
        AppCovid2.start_month_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid2.start_month_entry.set_completion_list(month_value)
        AppCovid2.start_month_entry.grid(row=1, column=1,
                                         sticky='nesw', padx=10, pady=10)
        AppCovid2.start_month_entry.insert(0, '04')

        # Create start year option:
        AppCovid2.start_year = ttk.Label(leftframe,
                                         text='Start Year:', font=10)
        AppCovid2.start_year.grid(row=2, column=0,
                                  sticky='nesw', padx=10, pady=10)
        AppCovid2.start_year_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid2.start_year_entry.set_completion_list(year_value)
        AppCovid2.start_year_entry.grid(row=2, column=1,
                                        sticky='nesw', padx=10, pady=10)
        AppCovid2.start_year_entry.insert(0, '2020')

        # Create end day option:
        AppCovid2.end_day = ttk.Label(leftframe, text='End Day:', font=10)
        AppCovid2.end_day.grid(row=3, column=0,
                               sticky='nesw', padx=10, pady=10)
        AppCovid2.end_day_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid2.end_day_entry.set_completion_list(day_value)
        AppCovid2.end_day_entry.grid(row=3, column=1,
                                     sticky='nesw', padx=10, pady=10)
        AppCovid2.end_day_entry.insert(0, '01')

        # Create end month option:
        AppCovid2.end_month = ttk.Label(leftframe, text='End Month:', font=10)
        AppCovid2.end_month.grid(row=4, column=0,
                                 sticky='nesw', padx=10, pady=10)
        AppCovid2.end_month_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid2.end_month_entry.set_completion_list(month_value)
        AppCovid2.end_month_entry.grid(row=4, column=1,
                                       sticky='nesw', padx=10, pady=10)
        AppCovid2.end_month_entry.insert(0, '08')

        # Create end year option:
        AppCovid2.end_year = ttk.Label(leftframe, text='End Year:', font=10)
        AppCovid2.end_year.grid(row=5, column=0,
                                sticky='nesw', padx=10, pady=10)
        AppCovid2.end_year_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid2.end_year_entry.set_completion_list(year_value)
        AppCovid2.end_year_entry.grid(row=5, column=1,
                                      sticky='nesw', padx=10, pady=10)
        AppCovid2.end_year_entry.insert(0, '2020')

        # Create area option:
        AppCovid2.area_1 = ttk.Label(leftframe, text='Area 1:', font=10)
        AppCovid2.area_1.grid(row=6, column=0, sticky='nesw', padx=10, pady=10)
        AppCovid2.area_1_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid2.area_1_entry.set_completion_list(area_list)
        AppCovid2.area_1_entry.grid(row=6, column=1,
                                    sticky='nesw', padx=10, pady=10)
        AppCovid2.area_1_entry.insert(0, 'Hartlepool')

        AppCovid2.area_2 = ttk.Label(leftframe, text='Area 2:', font=10)
        AppCovid2.area_2.grid(row=7, column=0, sticky='nesw', padx=10, pady=10)
        AppCovid2.area_2_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid2.area_2_entry.set_completion_list(area_list)
        AppCovid2.area_2_entry.grid(row=7, column=1,
                                    sticky='nesw', padx=10, pady=10)
        AppCovid2.area_2_entry.insert(0, 'Middlesbrough')

        # Create query button:
        query_button = ttk.Button(
                                  leftframe,
                                  text='Compare Daily Case', cursor='hand2',
                                  command=lambda:
                                  run_app1(AppCovid2.start_year_entry.get(),
                                           AppCovid2.start_month_entry.get(),
                                           AppCovid2.start_day_entry.get(),
                                           AppCovid2.end_year_entry.get(),
                                           AppCovid2.end_month_entry.get(),
                                           AppCovid2.end_day_entry.get(),
                                           AppCovid2.area_1_entry.get(),
                                           AppCovid2.area_2_entry.get()))
        query_button.grid(row=8, column=1, sticky='nesw', padx=10, pady=10)

        query_button = ttk.Button(
                                  leftframe,
                                  text='Compare by age group', cursor='hand2',
                                  command=lambda:
                                  run_app2(AppCovid2.start_year_entry.get(),
                                           AppCovid2.start_month_entry.get(),
                                           AppCovid2.start_day_entry.get(),
                                           AppCovid2.end_year_entry.get(),
                                           AppCovid2.end_month_entry.get(),
                                           AppCovid2.end_day_entry.get(),
                                           AppCovid2.area_1_entry.get(),
                                           AppCovid2.area_2_entry.get()))
        query_button.grid(row=9, column=1, sticky='nesw', padx=10, pady=10)

        # Create back button
        back_button = ttk.Button(
                                 leftframe, cursor='hand2', text='Back',
                                 command=lambda:
                                 controller.show_frame(StartPage))
        back_button.grid(row=8, column=0, sticky='nesw', padx=10, pady=10)

        # Create quit button
        quit_button = ttk.Button(
                                leftframe, cursor='hand2', text='QUIT',
                                command=controller.quit)
        quit_button.grid(row=9, column=0, sticky='nesw', padx=10, pady=10)

        # Call check format function
        # and run plot function for "Compare Daily case" button
        def run_app1(
                    start_year, start_month, start_day,
                    end_year, end_month, end_day, area_1, area_2):
            check_count = checkCovid.check_value2(
                                                 start_year, start_month,
                                                 start_day, end_year,
                                                 end_month, end_day,
                                                 area_1, area_2)
            if check_count == 0:
                plotCovid.plotCovid_20(
                                       start_year, start_month, start_day,
                                       end_year, end_month, end_day,
                                       area_1, area_2, rightframe)

        # Call check format function
        # and run plot function for "Compare by age group" button
        def run_app2(
                    start_year, start_month, start_day,
                    end_year, end_month, end_day, area_1, area_2):
            check_count = checkCovid.check_value2(
                                                 start_year, start_month,
                                                 start_day, end_year,
                                                 end_month, end_day,
                                                 area_1, area_2)
            if check_count == 0:
                plotCovid.plotCovid_21(
                                       start_year, start_month, start_day,
                                       end_year, end_month, end_day,
                                       area_1, area_2, rightframe)


""" Covid App - Dislay general covid information
in the UK for a given period """


class AppCovid3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        month_value = Covid_DropBoxOption.month_value
        day_value = Covid_DropBoxOption.day_value
        year_value = Covid_DropBoxOption.year_value

        title_label = tk.Label(
                                self, text='Covid Information',
                                borderwidth=5, relief='solid',
                                anchor='c', justify='center', font=20,
                                background='blue', foreground='white')
        title_label.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

        # Create left frame and right frame:
        leftframe = tk.Frame(self, width=200, height=500, bg='grey')
        leftframe.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        rightframe = tk.Frame(self, width=600, height=500, bg='white')
        rightframe.grid(row=1, column=1, sticky='nesw', padx=10, pady=10)

        # Create start day option:
        AppCovid3.start_day = ttk.Label(leftframe, text='Start Day:', font=10)
        AppCovid3.start_day.grid(row=0, column=0,
                                 sticky='nesw', padx=10, pady=10)
        AppCovid3.start_day_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid3.start_day_entry.set_completion_list(day_value)
        AppCovid3.start_day_entry.grid(row=0, column=1,
                                       sticky='nesw', padx=10, pady=10)
        AppCovid3.start_day_entry.insert(0, '01')

        # Create start month option:
        AppCovid3.start_month = ttk.Label(leftframe,
                                          text='Start Month:', font=10)
        AppCovid3.start_month.grid(row=1, column=0,
                                   sticky='nesw', padx=10, pady=10)
        AppCovid3.start_month_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid3.start_month_entry.set_completion_list(month_value)
        AppCovid3.start_month_entry.grid(row=1, column=1,
                                         sticky='nesw', padx=10, pady=10)
        AppCovid3.start_month_entry.insert(0, '04')

        # Create start year option:
        AppCovid3.start_year = ttk.Label(leftframe,
                                         text='Start Year:', font=10)
        AppCovid3.start_year.grid(row=2, column=0,
                                  sticky='nesw', padx=10, pady=10)
        AppCovid3.start_year_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid3.start_year_entry.set_completion_list(year_value)
        AppCovid3.start_year_entry.grid(row=2, column=1,
                                        sticky='nesw', padx=10, pady=10)
        AppCovid3.start_year_entry.insert(0, '2020')

        # Create end day option:
        AppCovid3.end_day = ttk.Label(leftframe, text='End Day:', font=10)
        AppCovid3.end_day.grid(row=3, column=0,
                               sticky='nesw', padx=10, pady=10)
        AppCovid3.end_day_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid3.end_day_entry.set_completion_list(day_value)
        AppCovid3.end_day_entry.grid(row=3, column=1,
                                     sticky='nesw', padx=10, pady=10)
        AppCovid3.end_day_entry.insert(0, '01')

        # Create end month option:
        AppCovid3.end_month = ttk.Label(leftframe, text='End Month:', font=10)
        AppCovid3.end_month.grid(row=4, column=0,
                                 sticky='nesw', padx=10, pady=10)
        AppCovid3.end_month_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid3.end_month_entry.set_completion_list(month_value)
        AppCovid3.end_month_entry.grid(row=4, column=1,
                                       sticky='nesw', padx=10, pady=10)
        AppCovid3.end_month_entry.insert(0, '08')

        # Create end year option:
        AppCovid3.end_year = ttk.Label(leftframe, text='End Year:', font=10)
        AppCovid3.end_year.grid(row=5, column=0,
                                sticky='nesw', padx=10, pady=10)
        AppCovid3.end_year_entry = tkec.AutocompleteCombobox(leftframe)
        AppCovid3.end_year_entry.set_completion_list(year_value)
        AppCovid3.end_year_entry.grid(row=5, column=1,
                                      sticky='nesw', padx=10, pady=10)
        AppCovid3.end_year_entry.insert(0, '2020')

        # Create query button:
        query1_button = ttk.Button(
                                  leftframe,
                                  text='Region Query', cursor='hand2',
                                  command=lambda:
                                  run_app1(AppCovid3.start_year_entry.get(),
                                           AppCovid3.start_month_entry.get(),
                                           AppCovid3.start_day_entry.get(),
                                           AppCovid3.end_year_entry.get(),
                                           AppCovid3.end_month_entry.get(),
                                           AppCovid3.end_day_entry.get()))
        query1_button.grid(row=8, column=1, sticky='nesw', padx=10, pady=10)

        query2_button = ttk.Button(
                                  leftframe,
                                  text='Top 5 UTLA Query', cursor='hand2',
                                  command=lambda:
                                  run_app2(AppCovid3.start_year_entry.get(),
                                           AppCovid3.start_month_entry.get(),
                                           AppCovid3.start_day_entry.get(),
                                           AppCovid3.end_year_entry.get(),
                                           AppCovid3.end_month_entry.get(),
                                           AppCovid3.end_day_entry.get()))
        query2_button.grid(row=9, column=1, sticky='nesw', padx=10, pady=10)

        query3_button = ttk.Button(
                                  leftframe,
                                  text='Top 5 ITLA Query', cursor='hand2',
                                  command=lambda:
                                  run_app3(AppCovid3.start_year_entry.get(),
                                           AppCovid3.start_month_entry.get(),
                                           AppCovid3.start_day_entry.get(),
                                           AppCovid3.end_year_entry.get(),
                                           AppCovid3.end_month_entry.get(),
                                           AppCovid3.end_day_entry.get()))
        query3_button.grid(row=10, column=1,
                           sticky='nesw', padx=10, pady=10)

        query4_button = ttk.Button(
                                  leftframe,
                                  text='Daily cases in the UK ',
                                  cursor='hand2',
                                  command=lambda:
                                  run_app4(AppCovid3.start_year_entry.get(),
                                           AppCovid3.start_month_entry.get(),
                                           AppCovid3.start_day_entry.get(),
                                           AppCovid3.end_year_entry.get(),
                                           AppCovid3.end_month_entry.get(),
                                           AppCovid3.end_day_entry.get()))
        query4_button.grid(row=11, column=1,
                           sticky='nesw', padx=10, pady=10)

        # Create back button
        back_button = ttk.Button(
                                 leftframe, cursor='hand2', text='Back',
                                 command=lambda:
                                 controller.show_frame(StartPage))
        back_button.grid(row=8, column=0, sticky='nesw', padx=10, pady=10)

        # Create quit button
        quit_button = ttk.Button(
                                leftframe, cursor='hand2', text='QUIT',
                                command=controller.quit)
        quit_button.grid(row=9, column=0, sticky='nesw', padx=10, pady=10)

        # Call check format function and
        # Plot Covid case by region in a given period:
        def run_app1(start_year, start_month, start_day,
                     end_year, end_month, end_day):
            check_count = checkCovid.check_value3(
                                                 start_year, start_month,
                                                 start_day, end_year,
                                                 end_month, end_day)
            if check_count == 0:
                plotCovid.plotCovid_30(
                                       start_year, start_month,
                                       start_day, end_year,
                                       end_month, end_day, rightframe)

        # Call check format function and
        # Plot top 5 UTLA Covid cases
        def run_app2(start_year, start_month, start_day,
                     end_year, end_month, end_day):
            check_count = checkCovid.check_value3(
                                                 start_year, start_month,
                                                 start_day, end_year,
                                                 end_month, end_day)
            if check_count == 0:
                plotCovid.plotCovid_31(
                                       start_year, start_month,
                                       start_day, end_year,
                                       end_month, end_day, rightframe)

        # Call check format function and
        # Plot top 5 UTLA Covid cases
        def run_app3(start_year, start_month, start_day,
                     end_year, end_month, end_day):
            check_count = checkCovid.check_value3(
                                                 start_year, start_month,
                                                 start_day, end_year,
                                                 end_month, end_day)
            if check_count == 0:
                plotCovid.plotCovid_32(
                                       start_year, start_month,
                                       start_day, end_year,
                                       end_month, end_day, rightframe)

        # Call check format function and
        # Daily cases in the UK
        def run_app4(start_year, start_month, start_day,
                     end_year, end_month, end_day):
            check_count = checkCovid.check_value3(
                                                  start_year, start_month,
                                                  start_day, end_year,
                                                  end_month, end_day)
            if check_count == 0:
                plotCovid.plotCovid_33(
                                       start_year, start_month,
                                       start_day, end_year,
                                       end_month, end_day, rightframe)


# Main program
if __name__ == "__main__":
    app = root()
    app.mainloop()
