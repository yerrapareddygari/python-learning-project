import random
import math
import datetime
import calendar
import os

places = ["AP","KA","TN","KL","MA"]

result = random.choices(places)
print(result)


#-------------------------------------------
rads = math.radians(90)
print(rads)
print(math.sin(rads))

#----------------------------------------
today = datetime.date.today()
print(today)

print(calendar.isleap(2017))  # to check the year is leap year or not !!

#-----------------------------------------
print(os.__file__)


#-------------------PIP INFO--------------------------------------

"""
1.pip --help  : To get the help of the commands.
2.pip install --help : To get the information of the install.
3.pip uninstall numpy : To uninstall a package.
4.pip list : To get the list of packages installed.
5.pip list ==outdated : To get the list of outdated packages.
6.pip install -U numpy : To update the package to the latest version.
7.pip install -r requirements.txt : To install all the packages inside the text file.
8.pip freeze > requirements.txt : To add the required packages to .txt file.
9.pip install pip-upgrader and run pip-upgrade : This will install a package which will update all the 
  packages to latest version.
10.pip install virtualenv : To install virtualenv package.

"""

# ---------------------------------------------SUMMARY------------------------------------------------------

"""
1.All about imports.
2.Usage of pip.
"""