# GITHUB USER DATA

## DESCRIPTION

*It is a simple Django based website project that combines both front-end and back-end technologies to provide an interface to the user where he can get information about his Github account on entering his Github username*


## DETAILED DESCIPTION

The Github username supplied by the user is sent to the external github API 
'''https://api.github.com/search/users'''.
From the obtained JSON data, "username","blog_url" and "score" is displayed to the user.


## Technologies used

1. Django 2.2.4,Django Rest Framework 3.10.2

1. Python (Django framework uses Python) 3.7.3

## How to set up the project

1. Install Python from this link from here :https://www.python.org/downloads/
1. On terminal, type ```pip install virtualenv``` to install virtual environment.
1. Run the command ```virtualenv my_name```. After running this command, a directory named "my_name" will be created that will contain all the necessary executables to use the packages a Python project would need.
1. Activate this virtual environment using the command ```./Scripts/activate```. The name of your virtual environment will now appear on the left side of terminal. 
1. Install django using ```pip install django==3.9.4```.
1. Install django rest framework using ```pip install djangorestframework==3.7.3```.
1. Install Python's requests module using ```pip install requests```.
