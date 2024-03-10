# Task 5: Capstone Project

# 
#
#

import math 

"""

Pseudo code 

User input - prompt user to determine which calculation they would like to use (investment or bond).
Convert the user input into lowercase, so that code can recognise the word regardless of capitising.

Determine if the user wants to use investement, by users input.
    
    Determine the parameters used for the investment calcultion, by prompting user for input.
             
             if the user wants to use simple interest.
             Calculate the simple interest.
             Print the Result.
             
             else if the user wants to use compound interest.
             Calculate the compound interest.
             Print the Result.

Determine else if the user wants to use the bond repayment calculator, by userss input.

    Detremine the paramters used for the bond repayment calculation, by prompting user for input.
    Calculate the bond repayment.
    Print out the results.

Else if the user input is invalid 
     Print out error message


"""

# # # User Input to identify which calculation (investment or bond) is required.

program = input("Hello, would you like to calculate your Investment or Bond ? If so, please input Investment or Bond in the answer. " ).lower() # Converts input into lowercase, so that any form of capatilising would be recognised.


# # # Using users input to determine which follow up questions to ask to gain required parameters for calculation.

# # if the user was to input investment, the code would output the following questions 
if program == "investment":

    # Determining the paramaters for the investment calcultion
    A = int(input("Input the amount of the investment. "))    
    s = int(input("Input the rate of interest on the investment. ")) 
    t = int(input("Input the number of years of investment. "))
    r = s/100 # Converts the interest rate from percentage

    # Determing which interest to be apply to calculate the total investment 
    variable = input("Input which type of interest taken on the investment (simple or compound). ").lower()

    # The required calculation if the interest is simple or else if the interest is compound.
    if variable == "simple":
       simple_interest = A*(1+r*t) # Calculation for simple interest
       print("The investment total is",simple_interest,"after",t,"years.") # Prints out the required output for user.
    elif variable == "compound":
        compound_interest =  A * math.pow((1+r),t) # Calculation for compound interest 
        print("The investment total is",compound_interest,"after",t,"years.") # Prints out the required output for user.


# # Else if the user was to input bond, the following question would be asked to calculate the bond repayment     
elif program == "bond":
    P = int(input("Input the current value of the house. "))                  # The paramaters required for bond repayment calculation
    m = int(input("Input the interest rate. "))                               # The paramaters required for bond repayment calculation
    n = int(input("Input the number of months needed to repay the bond. "))   # The paramaters required for bond repayment calculation
    i = m / 1200 # Converts the interest to monthly interest 

    # Bond repayment calculation
    bond = (i * P)/(1 - (1 + i)**(-n)) # Calculation for bond repayment 
    print("The payment of",bond,"needs to be made every month.")


# # Else the user input an inavlid answer, terminating the operation
else:
    print("Invalid answer. Please specify bond or investment. ") # Prints the error for user to see





