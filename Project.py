town = str(input())
commission = -1.0
sales = float(input())
if town == "Sofia":
    if sales >=0 and sales <=500:commission = 0.5
    elif sales > 500 and sales <= 1000:commission = 0.07
    # ToDo

elif town == "Varna":
elif town == "Plovdiv":
if commission >= 0:
    print(f"{sales * commission:.2f}")

else:
    print("error")