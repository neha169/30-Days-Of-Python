##level1
#1
list1=[]

#2
list2=[1,2,3,4,5]

#3
print(len(list2))

#4
print(list2[0])
print(list2[2])
print(list2[-1])

#5
mixed_data_types=['neha',24, 5.1,"single","mumbai"]

#6
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7
print(it_companies)
print(mixed_data_types)

#8
print(len(it_companies))

#9
print(it_companies[0])
print(it_companies[3])  
print(it_companies[-1])

#10
it_companies[0]='Meta'

#11
print(it_companies)

#12
it_companies.insert(3,'Twitter')

#13
upper_case_companies=[company.upper() for company in it_companies]
print(upper_case_companies)

#14
joined_string='#'.join(it_companies)
print(joined_string)

#15
has_apple='Apple' in it_companies
print(has_apple)

#16
print(it_companies.sort())

#17
reverse_sorted_companies=sorted(it_companies,reverse=True)
print(reverse_sorted_companies)

#18
first_three_companies=it_companies[:3]
print(first_three_companies)

#19
last_three_companies=it_companies[-3:]  
print(last_three_companies)

#20
middle_company=it_companies[len(it_companies)//2]
print(middle_company)

#21
it_companies.pop(0)

#22
it_companies.pop(len(it_companies)//2)

#23
it_companies.pop(-1)

#24
it_companies.clear()

#25
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list=front_end+back_end
print(joined_list)

#26
full_stack=joined_list.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

#level2
#1
age = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sorted_age=sorted(age)
print(sorted_age)
print(min(age))
print(max(age))

#2
median_age=sorted_age[len(sorted_age)//2]
print(median_age)

#3
average_age=sum(age)/len(age)
print(average_age)

#4
range_of_age=max(age)-min(age)
print(range_of_age)

#5
abs_diff_min_avg=abs(min(age)-average_age)
abs_diff_max_avg=abs(max(age)-average_age)
print(abs_diff_min_avg)
print(abs_diff_max_avg)

#6
countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries)
un_countries=['China', 'Russia', 'USA']
scandinavian_countries=['Finland', 'Sweden', 'Norway', 'Denmark']
print(un_countries)
print(scandinavian_countries)

