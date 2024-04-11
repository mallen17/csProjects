#File: HW2.py
#Author: Max ALlen
#UT EID: mca2773
#Course: CS303E

import math
import random

#Question 1
radius = eval(input("Enter the radius of the pentagon: "))
p_side = 2 * radius * math.sin(math.pi/5)
p_area = round(5/(4 * math.sqrt(5 - 2 * math.sqrt(5))) * (p_side ** 2), 2)
print(f"The area of the pentagon is {p_area:.2f} units squared.")
print()
#Question 2
name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked this week: "))
pay_rate = eval(input("Enter hourly pay rate: "))
fed_tax = eval(input("Enter federal tax witholding rate (%): "))
state_tax = eval(input("Enter state tax witholding rate (%): "))
print()
# Here I have to make the sentences into variables so I'm able to align
# the spaces correctly and keep the dollar sign for the number.
gross = pay_rate * hours
fed = fed_tax/100 * gross
state = state_tax/100 * gross
hours_sentence = "Hours Worked:"
rate_num = f"${pay_rate:.2f}"
pay_num = f"${gross:.2f}"
fed_num = f"${fed:.2f}"
state_num = f"${state:.2f}"
# Combine the sentences and numbers and format
print(f"Weekly Pay Statement for {name}")
print(f"{hours_sentence:s}{hours:>9.1f}")
print(f"Pay Rate:{rate_num:>13}")
print(f"Gross Pay:{pay_num:>12}")
print("Deductions:")
print(f"  Federal Withholding ({fed_tax}%):{fed_num:>8}")
print(f"  State Withholding ({state_tax}%):{state_num:>9}")
print(f"Net Pay: ${(gross-fed-state):.2f}")
print()
#Question 3
rps = random.randint(0,2)
if rps == 0:
    rps = "rock"
if rps == 1:
    rps = "paper"
if rps == 2:
    rps = "scissors"
user = input("Choose rock, paper, or scissors: ")
print(f"Computer is {rps}. You are {user}.")
if rps == user:
    print("Draw.") 
if rps == "rock":
    if user == "paper":
        print("You win.")
    if user == "scissors":
        print("Computer wins.")
if rps == "paper":
    if user == "scissors":
        print("You win.")
    if user == "rock":
        print("Computer wins.")
if rps == "scissors":
    if user == "rock":
        print("You win.")
    if user == "paper":
        print("Computer wins.")
print()
