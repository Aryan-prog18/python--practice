#concepts we are going to use are find(), endswith().

Email = input("Enter your Email address here: ")
if '@' in Email and Email.endswith("gmail.com"):
    print("The email address you entered is valid")
else:
    print("The email address you entered is not valid\n please enter a valid email address")
    