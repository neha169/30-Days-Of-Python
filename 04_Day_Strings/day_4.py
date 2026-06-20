#1
str1='Thirty'
str2='Days'
str3='Of'
str4='Python'
str5=str1+" "+str2+" "+str3+" "+str4
print(str5)

#2
st1='Coding'
st2='For'  
st3='All'
st4=st1+" "+st2+" "+st3
print(st4)

#3
company="Coding For All"
print(company)

#4
length=len(company)
print(length)

#5
upper_case=company.upper()
print(upper_case)

#6
lower_case=company.lower()
print(lower_case)

#7
title_case=company.title()
print(title_case)
capitalize_case=company.capitalize()
print(capitalize_case)
swap_case=company.swapcase()
print(swap_case)

#8
slice=company[:1]
print(slice)

#9
index=company.index("Coding")
print(index)
find=company.find("Coding")
print(find)

#10
replace=company.replace("Coding","Python")
print(replace)

#11
replace_all=company.replace("Coding For All","Python For Everyone")
print(replace_all)
swap=company.replace("Coding For All","Python For Everyone")
print(swap)

#12
split=company.split()
print(split)

#13
str1="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_str1=str1.split(",")
print(split_str1)

#14
print(company[0])

#15
print(company[-1])

#16
print(company[10])

#17
print(company[0:6])

#18
print(''.join(word[0].upper() for word in "Python For Everyone".split()))

#19
print(''.join(word[0].upper() for word in "Coding For All".split()))

#20
print(company.index("C"))

#21
print(company.index("F"))

#22
print(company.rindex("l"))

#23
sentence="You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
print(sentence.find("because"))

#24
print(sentence.rindex("because"))

#25
slice_sentence=sentence[sentence.index("because"):sentence.rindex("because")+find("because")]
print(slice_sentence)

#26
print(sentence.strip("because"))

#27


#28
substring="Coding For All"
print(substring.startswith("Coding"))

#29
print(substring.endswith("All"))

#30
sentence="   Coding For All      "
print(sentence.strip())

#31
identifier="30DaysOfPython"
print(identifier.isidentifier())
identifier2="thirty_days_of_python"
print(identifier2.isidentifier())

#32
library=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(library))

#33
line="I am enjoying this challenge.\nI just wonder what is next."
print(line)

#34
sentence="Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(sentence)

#35
string_formatting="The area of a circle with radius {} is {} meters square."
radius=10
area=3.14*radius**2
print(string_formatting.format(radius, area))

#36
num1=5
num2=4
print("{} + {} = {}".format(num1, num2, num1+num2))
print("{} - {} = {}".format(num1, num2, num1-num2))
print("{} * {} = {}".format(num1, num2, num1*num2))
print("{} / {} = {}".format(num1, num2, num1/num2))
print("{} % {} = {}".format(num1, num2, num1%num2))
print("{} // {} = {}".format(num1, num2, num1//num2))
print("{} ** {} = {}".format(num1, num2, num1**num2))




