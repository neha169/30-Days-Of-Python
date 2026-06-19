age=24
height=5.2
A=2+3j
b=input("Enter base of the triangle: ")
h=input("Enter height of the triangle: ")
area=0.5*float(b)*float(h)
print("Area of the triangle is:",area)

side_a=int(input("\n Enter side a of the triangle: "))
side_b=int(input("Enter side b of the triangle: "))   
side_c=int(input("Enter side c of the triangle: "))
perimeter=side_a+side_b+side_c
print("Perimeter of the triangle is:",perimeter)

length=int(input("Enter length of the rectangle: "))
width=int(input("Enter width of the rectangle: "))
area_rectangle=length*width
print("Area of the rectangle is:",area_rectangle)

radius=int(input("Enter radius of the circle: "))
pi=3.14 
area_circle=pi*radius**2
print("Area of the circle is:",area_circle)
circumference_circle=2*pi*radius
print("Circumference of the circle is:",circumference_circle)

print(len('python'))
print(len('dragon'))
print(len('python') == len('dragon'))
print(len('python') > len('dragon'))

print('on' in 'python')
print('on' in 'dragon')

sentence="I hope this course is not full of jargon"
print('jargon' in sentence)

print('on' not in 'python')
print('on' not in 'dragon')

print(len('python'))
print(float(len('python')))
print(str(len('python')))

print(7//3)
print(2.7)
print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

hours = float(input('Enter hours: '))
rate  = float(input('Enter rate per hour: '))
print(f'Your weekly earning is {hours * rate:.0f}')

years = int(input('Enter number of years you have lived: '))
secs  = years * 365 * 24 * 60 * 60
print(f'You have lived for {secs} seconds.')

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)






