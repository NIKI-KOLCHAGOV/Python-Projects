number = int(input("Number :"))
valid = number >= 100 and number <= 200 or number == 0
print(valid)
if not valid:
    print("invalid")

else:
    print("valid")
