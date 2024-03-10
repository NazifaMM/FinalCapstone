# Task 1

# Pseudo code 
"""
Request input from user and store it as a variable called age. 
if age is between >= 65 and <= 100, output "Enjoy your retirement!"
else if the age >= 40  and < 65, output "You are over the hill"
else output " Age is but a number"
if age > 100, output "You are dead" 
if age is < 13, ouput " You qualify for the kiddie discount"
if age == 21,  output "Congrats on your 21st!" 

"""

age = int(input("what is your age? " )) # Input from user 

if age >= 65 and age <= 100 :           # if age is between >= 65 and <= 100, output "Enjoy your retirement!"
    print("Enjoy your retirement!")    

elif age >= 40 and age < 65 :           # else if the age >= 40  and < 65, output "You are over the hill"
    print(" You are over the hill") 

else:                                   # else output " Age is but a number"
    print("Age is but a number")

     
if age == 21:                           # if age == 21,  output "Congrats on your 21st!" 
    print("Congrats on your 21st!")

if age < 13:                            # if age is < 13, ouput " You qualify for the kiddie discount"
    print(" You qaulify for the kiddie discount")   

if age > 100 :                          # if age > 100, output "You are dead"
    print("You are dead")

