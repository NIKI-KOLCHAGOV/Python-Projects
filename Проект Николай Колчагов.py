#Програма за изчисляване на комисионна
#От Николай Колчагов @NIKI-KOLCHAGOV
print("\033[0;31;33mHello Здравейте :D\033[00m"); print("\033[1;31;32m$ Програма За Изчисляване На Комисионна $\033[00m"); print("\033[0;31;36m------------------------------------------")

try:
    Town = str(input("Град: "))
except KeyboardInterrupt:
    print(""); print("Благодаря Че Ползвахте"); print("-"); print("\033[1;31;33mОт @NIKI-KOLCHAGOV"); exit()
while not Town == "Sofia" or Town == "Plovdiv" or Town == "Varna":
    try:
        print("\033[1;31;33mВъведената от вас информация е грешна\033[00m"); print("\033[4;31;32mВъведете Един от посочените Градове Спазваите големината на буквите\033[00m"); print("\033[3;31;36mSofia, Varna, Plovdiv\033[00m")
        Town = str(input("Град: "))
    except KeyboardInterrupt:
        print(""); print("Благодаря Че Ползвахте"); print("-"); print("\033[1;31;33mОт @NIKI-KOLCHAGOV"); exit()
while True:
    try:
        Sales = float(input("Продажби: ")); break
    except ValueError:
        print("\033[1;31;33mВъведената от вас информация е грешна\033[00m"); print("\033[4;31;32mТрябва да въведете Число без други неща\033[00m")
    except KeyboardInterrupt:
        print(""); print("Благодаря Че Ползвахте"); print("-"); print("\033[1;31;33mОт @NIKI-KOLCHAGOV"); exit()
Dict = {"Sofia" : 1, "Plovdiv" : 2, "Varna" : 3}
Town = Dict[Town]
myDict = {1: [5, 7, 8, 12],2: [5.5, 8, 12, 14.5],3: [4.5, 7.5, 10, 13]}
Town = myDict[Town]
count = 0; number = 0; Prices = {0: 0, 1: 501, 2: 1001, 3: 10001}
while (count < 4):
    if Sales >= Prices[count]:
        Results = Sales * Town[count] / 100; tax = Town[count]
    count = count + 1
print("\033[0;31;36m------------------------------------------"); print("\033[1;31;33mЗа продажби от", Sales, "лв комисионната такса е", tax,"%")
print('\033[1;31;32m↳',round(Results, 2), "лв комисионна такса"); print("\033[0;31;34mОбща сума с комисионна такса:\033[1;31;32m", round(Sales - Results, 2), "лв\033[00m")

#Old Code (Not Correct)
#while (count < 20):
#    count = count + 1
#    if Sales >= number:
#        Final = round(count / 5 - 1)
#        Results = Sales * Town[Final] / 100
#    number = number + 500
#print("-"); print("За продажби от", Sales, "комисионната такса е", Town[Final],"%")
#print(Results)
