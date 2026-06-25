#level1
#1
age=int(input("Enter your age:"))
if age >=18:
    print("You are old enough to drive")
else:
    year=18-age
    print(f"You need {year} more years to learn to drive")

#2
my_age=24
your_age=int(input("Enter your age:"))

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print(f"You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")

elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print(f"You are 1 year younger than me.")
    else:
        print(f"You are {difference} years younger than me.")

else:
    print("We are the same age!")

#3
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

#level2
#1
score = float(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 0:
    print("Grade: F")
else:
    print("Invalid score!")

#2
month = input("Enter a month: ").strip().capitalize()

if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month!")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(f"Updated list: {fruits}")

#level3
#1
person = {
    'first_name': 'Neha',
    'last_name': 'Nirmmal',
    'age': 24,
    'country': 'India',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'FastAPI', 'MongoDB', 'Python'],
    'address': {
        'street': 'Jawhar nagar',
        'zipcode': '400051'
    }
}

# 1. Print middle skill
if 'skills' in person:
    skills = person['skills']
    middle = skills[len(skills) // 2]
    print(f"Middle skill: {middle}")

# 2. Check if Python is in skills
if 'skills' in person:
    if 'Python' in person['skills']:
        print("This person knows Python!")
    else:
        print("This person does not know Python.")

# 3. Developer title
if 'skills' in person:
    skills = set(person['skills'])
    if skills == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'FastAPI', 'Python', 'MongoDB'}.issubset(skills):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# 4. Married and lives in Finland
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
