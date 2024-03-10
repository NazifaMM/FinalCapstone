# Task 2 

# # # Scenario

#  User inputs the date of birth 
#  Outputs a message stating where they are , a winter/summer/spring/autumn baby 
#
# # How the code would look like without a logical error:
#
#
# season = input("Which month were you born ? ").lower()   # User input 
#
# Using if and elif statements so the code can recognise the seasons
#
# if season == "december" or season == "january" or season == "february":
#    print("You are a winter baby!")                                             
#
# elif season == "march" or season == "april" or season == "may":
#    print("You are a spring baby!")
#
# elif season == "june" or season == "july" or season == "august":
#    print("You are a summer baby!")
#
# elif season == "september" or season == "october" or season == "november": 
#    print("You are a autumn baby!")
#
# else:
#    print("Invalid input. Please input a valid month.")    # Prints out error message if anything other than the months is inputed


# Error code 


season = input("Which month were you born ? ").lower()

if season == "december" and season == "january" and season == "february":  # error uses and instead of or 
    print("You are a winter baby!")                                             

elif season == "march" and season == "april" and season == "may":
    print("You are a spring baby!")

elif season == "june" and season == "july" and season == "august":
    print("You are a summer baby!")

else:                                        # Doesn't account for error inputs
    print("You are a autumn baby!")
























