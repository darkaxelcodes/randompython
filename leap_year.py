def leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

year = int(input("Enter the year to check for Leap Year: "))
result = leap_year(year)
if result:
    print("The year {} is a leap year.".format(year))
else:
    print("The year {} is NOT a leap year.".format(year))