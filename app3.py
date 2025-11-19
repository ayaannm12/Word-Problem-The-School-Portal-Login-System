
password = None


email = str(input("what is your email???")).strip()
if "@" not in email:
    print("email not valid there is no @ symbol!!")
else:
    print("Your email is valid, thank you!")
password = str(input("what would you like your password to be??"))
is_valid_password = True
if len(password) < 8:
     print("password is not valid, its too short 8 characters are the minimum!!!")
     is_valid_password = False
if not any(char.isdigit() for char in password):
     print("Your password is not valid you need atleast one number!!!")
     is_valid_password = False
    
if not any(char.isupper() for char in password):
    print("Password is not valid you need atleast one uPper case letter!!!!")
    is_valid_password = False

if is_valid_password:
     print("Your password is valid, thank you!")


print("They both are valid here's your info:")
print("Username:", email)
print("Password:", password)