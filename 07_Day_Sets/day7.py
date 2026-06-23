# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#level1
#1
length=len(it_companies)
print(length)

#2
it_companies.add('Twitter')
print(it_companies)

#3
it_companies.update(["infosys","uber","cisco"])
print(it_companies)

#4
it_companies.remove("uber")
print(it_companies)

#5
"""
remove() is strict: It deletes the item. If the item is not there, it crashes your program with an error.discard() is relaxed: It deletes the item. If the item is not there, it does nothing and your program keeps running.

"""
it_companies.remove("infosys")
it_companies.discard("uber")

#level2
#1
C=A.union(B)
print(C)

#2
INTER=A.intersection(B)
print(INTER)

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
print(A.union(B))
print(B.union(A))

#6
print(A.symmetric_difference(B))

#7
del A

