#level1
#1
def _add_two_numbers_(num1,num2):
    sum=num1+num2
    return sum
print("sum is",_add_two_numbers_(3,6))

#2
def _area_of_circle_(r):
    π=3.14
    area = π * r * r
    return area
ra=int(input("enter radius:"))
print("area is",_area_of_circle_(ra))

#3
def add_all_nums(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Error: '{arg}' is not a number. All arguments must be numeric."
    total = 0
    for arg in args:
        total += arg
    return total

#4
def _convert_celsius_to_fahrenheit_(C):
    F = (C * 9/5) + 32
    return F
c=int(input("Enter celsius:"))
print("Temperature in °C can be converted to °F:",_convert_celsius_to_fahrenheit_(c))

#5
def check_season(month):
    month = month.strip().capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month. Please enter a valid month name.'
m=input("Enter month:")
print(check_season(m))

#6
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'Undefined (vertical line)'
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(1, 2, 3, 6)) 

#7

#8
def print_list(lst):
    for item in lst:
        print(item) 




