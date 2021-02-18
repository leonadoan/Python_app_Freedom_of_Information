FREEDOM OF INFORMATION APP 

Created by LE MINH THAO DOAN, 14/01/2021


CONTENTS OF THIS FILE
---------------------

 * Quick Guides
 * Introduction
 * Requirements
 * Notices


QUICK GUIDES
--------------

How To Run "Freedom of Information (FOI) app":

    1. Open "GUI.py" in the Source folder with your IDE
    2. Simply click "Run" button on your IDE
    3. The app window will open and wait for your interaction

If you want to use the terminal to run "GUI.py", this command can be used:	
	
	python GUI.py (make sure your directory is in Source folder)

		

INTRODUCTION
------------

File structure of FOI app:

	Source/
	│
	├── GUI.py/  (main program, contain tkinter code for app GUI)
	│
        ├── README.txt
	│
	├── Support_modules/
	│    ├── __init__.py
	│    ├── app_function.py  (contain support function for other modules)
	│    ├── checkCovid.py 	  (contain check format function for Covid section)
	│    ├── checkSnS.py	  (contain check format function for Stop & Search section)
	│    ├── covid_class.py   (contain objects for getting data from query for Covid section)
	│    ├── Covid_DropBoxOption.py  (contain lists of options for drop box in Covid section)
	│    ├── plotCovid.py     (contain function for plotting in Covid section)
	│    ├── plotSnS.py       (contain function for plotting in Stop & Search section)
	│    ├── stop_search_class.py    (contain objects for getting data from query for Stop & Search section)
	│    ├── StopAndSearch_DropBoxOption.py   (contain lists of options for drop box in Stop & Search section)
    	│    └── tkentrycomplete.py	 (contain function to create an entry-box with "try to complete" ability, 
	│				  third-party module, created by Mitja Martini)
	│
	├── Data/
	│    ├── specimenDate_ageDemographic-unstacked.csv  (Covid data)
	│    └── teesside.png     (Teesside logo image, credit: tees.ac.uk)
	│    
	└── Unit_test/
	     ├── __init__.py
	     ├── Covid_01_03_test.csv    (expected output data frames for covid_class)
	     ├── Covid_Hartlepool_16-03_31-03_test.cvs   (expected output data frames for covid_class)
	     ├── test_app_function.py    (unittest for app_function)
	     ├── test_covid_class.py     (unittest for covid_class)
	     └── test_stop_search_class.py   (unittest for stop_search_class)



REQUIREMENTS
------------

The app was developed using python 3. Therefore it is recommend to use python 3 for accessing the app.

This app requires the installation of following libraries:

 * matplotlib
 * numpy
 * requests
 * pandas

command for installation: pip install library-name



NOTICES
-------

 * The app is recommended to open and run by Visual Studio Code
 * The app has been checked and runs well on both macOS (Mojave) and Windows 10.
 * Therefore, it is recommended to run this app on the above environments.
 * The size of the graph may be different depending on the operating environment of your computer.

 * The current time period covered by Stop and search API is from 12/2017 to 11/2020.
 * The covered period by API is changing overtime, so you should check the website https://data.police.uk/about/#stop-search
 * for the most latest information

 * For running the unittest and showing a detailed result, this command can be used: 
		python -m unittest -v + folder.file-name

 * Coverage.py (https://coverage.readthedocs.io) was use to measure code coverage of this app.
 * Install coverage: pip install coverage
 * code coverage of Python programs: coverage run -m unittest discover
 * to get report: coverage report -m
 * to get report HTML format: coverage html

 * All files were checked through flaxe8 (https://flake8.pycqa.org) to make sure their compliance with PEP8.
 * Install flake8: pip install flake8 
 * For checking, on the terminal window, typing: flake8 path/to/file.py




