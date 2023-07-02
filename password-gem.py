import random
import string

def generate_password(min_length, numbers=True, special_chars=True):
    # grab all the characters
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # add all the characters into 1 string depending on the choices of the user
    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special
    
    pwd = "" # password generated
    meets_criteria = False # the next loop will keep iterating until the criteria is set to true
    has_number = False # checks for any numbers in the password
    has_special = False # checks for any special characters in the password

    while not meets_criteria or len(pwd) < min_length:
       
        # new character is added randomnly from list of characters to the pwd
        new_char = random.choice(characters)
        pwd += new_char

        # checks to see if new_char is a number or special characters
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        # now we check if we meet to see if criteria has been met
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special
        # the reason for why we repeat meets_criteria is to catch whether numbers criteria has failed as meet_criteria would have been False
        # if we don't want numbers, meets_criteria would remained as True regardless and not affect has_special

    return pwd


min_length = int(input("Enter the mimimun length of your password: "))
want_numbers = input("Do you want to have numbers in your password? Please answer with yes or no ===> ").lower() == "yes"
want_special = input("Do you want to have special characters in your password? Please answer with yes or no ===> ").lower() == "yes"
pwd = generate_password(min_length, want_numbers, want_special)

print("Your password is:", pwd)
