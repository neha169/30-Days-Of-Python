#1
dog={}
print(type(dog))

#2
dog={"name":"bruno","color":"black","breed":"hybrid","legs":"4","age":"2months"}
print(dog)

#3
student={"first_name":"neha","last_name":"nirmal","age":"24","marital_status":"single","skill":"creativity","country":"India","city":"Mumbai"}

#4
print(len(student))

#5
value=student.values()
print(value)

#6
student["skill"]=("positivity")
print(student["skill"])

#7
keys=student.keys()
print(keys)

#8
values=student.values()
print(values)

#9
print(student.items())

#10
student.popitem()
print(student)

#11
del student
