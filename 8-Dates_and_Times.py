from datetime import datetime as dt

print(dt.now())
'''
%Y = 4 digit year
%m = 2 digit month
%d = 2 digit day
%H = 2 digit 24 hour hour
%M = 2 digit minute
%S = 2 digit second
    ISO "%Y-%m-%d %H:%M:%S"
'''

date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
print(date)
merica = dt.now().strftime("%A %B %d, %Y %I:%M %p %Z")
print(merica)