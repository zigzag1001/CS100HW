"""
Peter Saburov
CS 100 2022S Section 012
HW 03, Feb 13, 2023
"""

#1
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    if month[0].lower() == 'j':
        print(month)


#2
for i in range(1, 100):
    if i % 2 == 0 and i % 5 == 0:
        print(i)


#3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letter in horton:
    if letter in vowels:
        print(letter)


#4
import math

print("100! =", math.factorial(100))
print("log2 of 1,000,000 =", math.log2(1000000))
print("gcd of 63 and 49 =", math.gcd(63, 49))


#5
import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0)

t.penup()
t.goto(-300, 140)
t.pendown()

#equilateral triangle
for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.forward(100)
t.pendown()

#square
for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.forward(133)
t.pendown()

#regular pentagon
for i in range(5):
    t.forward(100)
    t.left(72)

t.penup()
t.goto(100, -100)
t.pendown()

#four concentric circles
for circle in [50, 100, 150, 200]:
    t.circle(circle)
    t.penup()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.pendown()

turtle.done()