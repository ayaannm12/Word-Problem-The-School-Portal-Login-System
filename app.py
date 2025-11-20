
email = str(input("what is your email???")).strip()
if "@" not in email:
        email == False
        print("email not valid there is no @ symbol!!")
if email == False:
        email = str(input("what is your email???")).strip()
if "@" in email:
    print("Your email is valid, thnak you!")
    email == True
if email == True:
        password = str(input("what would you like your password to be??"))
        if len(password) < 8:
                 print("password is not valid, its too short 8 characters are the minimum!")
                 password == False
        if any(not char.isdigit() for char in password):
                print("Your password is not valid, you need atleast one number!")
                password == False
        if any(not char.isupper() for char in password):
                 print("Password is not valid you need atleast one upper case nummber !")
                 password == False
if email == True and password == True:
        print("they both are valid heres your info:")
        print("Username", email)
        print("password", password)
        