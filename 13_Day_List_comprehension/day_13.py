#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
num=[i for i in numbers if i<=0]
print("negative and zero in the list:",num)

#2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
one_dimensional_list=[number for row in list_of_lists for number in row]
print(one_dimensional_list)

#3
result = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat = [
    [country.upper(), country[:3].upper(), city.upper()]
    for pair in countries
    for country, city in pair
]
print(flat)

#5
dicts = [
    {'country': country.upper(), 'city': city.upper()}
    for pair in countries
    for country, city in pair
]
print(dicts)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')],  [('Bill', 'Gates')]]

full_names = [
    f"{first} {last}"
    for pair in names
    for first, last in pair
]
print(full_names)

#7
slope     = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

print(slope(1, 2, 3, 6))       
print(intercept(1, 2, 3, 6))
