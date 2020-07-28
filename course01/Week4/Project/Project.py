"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates. Completed!
"""

import datetime
import calendar

def leap_year(year):
    """ 
    Determines if the inputted year is a leap year.
    """
    # we define that function to check if year is leap year
    if calendar.isleap(year):
        return True
    else:
        return False

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
    Returns:
      The number of days in the input month.
    """

    if month in [4, 9, 6, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2 and leap_year(year):
        return 29
    elif month == 2 and not leap_year(year):
        return 28
    else:
        return 0

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    max_days_in_month = days_in_month(year,month)
    if datetime.MINYEAR <= year <= datetime.MAXYEAR and 1 <= month <= 12 and 1 <= day <= max_days_in_month:
        return True
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2) :
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        diff = date2 - date1
        if (date2 > date1):
            return (diff.days)
        else:
            return 0
    else:
        return 0
        

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    today = datetime.date.today()
    return days_between(year, month, day, today.year, today.month, today.day)
