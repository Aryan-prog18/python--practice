password = input("Enter password to check: ")
has_upper = any(char.isupper()for char in password) #any (basically like a boolean fun prints "true" if there is any iterable object like list,string and tuple)
has_lower = any(char.islower()for char in password)
has_digit = any(char.isdigit()for char in password)

if len(password)>= 8 and has_upper and has_lower and has_digit:
    print("Strength of the password is strong")
else:
    print("Strenght is weak please choose a strong password")