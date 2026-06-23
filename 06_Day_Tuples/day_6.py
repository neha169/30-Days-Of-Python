#level 1
#1
tuple=()

#2
brother=("shubham","sahil","rohan","yash","sankalp")
sister=("shreya","rasika","apurva","vaishnavi")

#3
siblings=brother+sister
print(siblings)

#4
print(len(siblings))

#5
s=list[siblings]
s[0]="mr.manohar"
s[1]="mrs.shakuntala"
family=tuple(s)
print(family)


#level 2
#1
family_members = ("Anna", "Ben", "Charlie", "Mom", "Dad")
*siblings, mother, father = family_members
parents = [mother, father]
print(siblings)  
print(parents)   


#2
fruits=("apple","banana","mango","grapes","orange")
vegetables=("potato","tomato","onion","cabbage","carrot")
animal_products=("milk","cheese","yogurt","butter","cream")
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)

#3
food_stuff_lt=list[food_stuff_tp]
print(food_stuff_lt)

#4
slice=food_stuff_tp[0:6]
slice2=food_stuff_lt[0:5]
print(slice)
print(slice2)

#5
slice3=food_stuff_lt[0:3]
slice4=food_stuff_lt[-4:-1]
print(slice3)
print(slice4)

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
