import os
print("\x1b[1;32mLog-In\x1b[0m Or \x1b[1;31mSign-Up\x1b[0m")
Selection = str(input("Enter \x1b[1;32mL\x1b[0m to log in, \x1b[1;31mS\x1b[0m to Sign up: "))
if Selection == "S" or Selection == "s":
    os.system('cls')
    print("Sign Up")
if Selection == "L" or Selection == "l":
    print("works Log In")