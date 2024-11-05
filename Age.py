age = float(input("Възраст:"))
gender = input("пол:")
if gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
else:
    if age >= 16:
        print("Mr.")
    else:
        print("Mister")