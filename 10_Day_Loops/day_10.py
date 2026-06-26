#level1
#1
for i in range(11):
    print(i, end=' ')
print()
 
# while loop
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print()

#2
for i in range(10, -1, -1):
    print(i, end=' ')
print()
 
# while loop
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1
print()

#3
for i  in range(1,8):
    print("#" * i)
print("\n")

#4
for i in range(8):
    for j in range(8):
        print("#", end="")
    print()
print("\n")

#5
for i in range(11):
    print(f"{i} x {i} = {i * i}")
print("\n")

#6
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lang in languages:
    print(lang)
print("\n")

#7
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=' ')
print("\n")

#8
for i in range(0, 101):
    if i % 2 != 0:
        print(i, end=' ')
print("\n")

#level2
#1
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total}.\n")

#2
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.\n")

#level3
#1