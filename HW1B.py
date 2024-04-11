#File: HW2A
#Author: Max Allen
#UT EID: mca2773
#Course: CS303E
#This program answers various questions based
#around the input and elementary functions.
#Q1
name = input("What is your name? ")
print("Hello " + name + "! You have just delved into Python.")
print()
#Q2
temp = int(input("Enter a temperature in degrees Celsius: "))
tempf = 9/5 * float(temp) + 32
print(str(temp) + " Celsius is " + str(tempf) + " Fahrenheit.")
print()
#Q3
bill, rate = eval(input("Enter the bill and gratuity rate: "))
gratuity = (bill) * (rate) * .01
total = gratuity + (bill)
print("The gratuity is $" + str(round(gratuity, 2)) + " and the total is $" \
      + str(round(total, 2)) + ".")
print()
#Q4
num = int(input("Enter a nuber between 0 and 999: "))
sum = (num // 100) + (num % 100 // 10) + (num % 10)
print("The sum of the digits is " + str(sum) + ".")
print()
#Q5
amount = int(input("Enter you investment amount ($): "))
years = int(input("Enter you investment length (years): "))
money_return = amount * (1.07) ** years
print("After " + str(years) + " years, you will have $" + str(round(money_return, 2)) \
      + ".")
print()
#Q6
age = int(input("Enter your age: "))
max_hr = 220 - age
low_hr, high_hr = max_hr * .5, max_hr * .85
print("Your target heart rate is " + str(round(low_hr)) + " - " \
      + str(round(high_hr)) + " bpm.")


