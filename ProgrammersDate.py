#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
#  1700 to 1917 --- Julian calendar
#  1919 --- Gregorian calendar 

#  leap years are divisible by 4. -- Julian 
#  Gregorian calendar leap years : divisible by 400 and divisible by 4 and not divisible by 100 

# Since the next day of the 31st January is 14th Febuary and the 32 day in the Russian calendar. We need to deduct 14 from the total date for only 1918. This is a special case 


def dayOfProgrammer(year):
    # Write your code here
    constant_year = 31 + 31 + 30 + 31 + 30 + 31 + 31
    programmer_year = 256
    reminder_days = 0
    if year <= 2700 and year >= 1700:
        if year > 1918 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            reminder_days = programmer_year-(constant_year + 29)
            return f'{reminder_days}.09.{year}' 
        else: 
            if (year < 1918) and (year % 4 == 0):
                reminder_days = programmer_year-(constant_year + 29)
                return f'{reminder_days}.09.{year}' 
            if (year == 1918):
                reminder_days = programmer_year-(constant_year + 29-14)
                return f'{reminder_days}.09.{year}'
                
            reminder_days = programmer_year-(constant_year + 28)
            return f'{reminder_days}.09.{year}' 
            
    else: 
        return ""
                    
