"""This code determines whether a year is a leap year and finds the number of days of a given month"""

# Number of days per month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
  """Returns True for leap years, False for non-leap years"""

  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
  """Return number of days in that month in that year."""
  
  if not 1 <= month <= 12:
    return 'Invalid MOnth'
  
  if month == 2 and is_leap(year):
    return 29
  
  return month_days[month]

#print(days_in_month(2023, 2))
