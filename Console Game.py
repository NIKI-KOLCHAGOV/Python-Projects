from NikisColorizer import *
from random import randrange
import time
import keyboard

#Apple Rush a Game About Collecting Apples
#By @NIKI-KOLCHAGOV
#
#Controls: Move with WASD
#Pick Up Enough Apples To Survive Winter Time
#And Dodge The Obstacles To Survive

def UpdateScreen():
    print(""); print(""); print("\033[3;31;33mNikis Games | \033[3;31;37mBy @NIKI-KOLCHAGOV\033[00m"); print("\033[1;31;31mApple\033[1;31;32m Rush"); print("Collect The \033[1;31;31m🍎 Apples \033[1;31;32mTo Survive \033[1;31;36mWinter Time");

global Season
Season = "Spring"

#Difficulty = int(input("Difficulty: "))
Difficulty = 12
GameGrid = Difficulty
Dict = ["🌳", "🍀", "🌿", "🌳", "🍀", "🌿", "🍎"]
Dict3 = ["🌳", "🍀", "🌿", "🌳", "🍀", "🌿"]
Dict4 = ["⬜", "🧊", "⛄", "⬜", "⬜", "🧊", "⬜"]
Dict2 = {0: ""}

Row = ""
for Counter2 in range(0, Difficulty, 1):
    print(Dict2[Counter2]);
    Row = ""
    for Counter in range(0, Difficulty, 1):
        Emoji = randrange(0, 7)
        Row = Row + Dict[Emoji]
    Dict2[(Counter2 + 1)] = Row
print(Dict2[Counter2]);
print(Dict2);


print(""); print(""); print(""); print(""); print("");
print("\033[1;31;31m           ,ggg,                                           ""\033[1;31;32m    ,ggggggggggg,                                    ", "     \033[3;31;33mNikis Games | \033[3;31;37mBy @NIKI-KOLCHAGOV\033[00m");
print("\033[1;31;31m          dP``8I                           ,dPYb,          ""\033[1;31;32m   dP```88``````Y8,                        ,dPYb,    ", "     \033[1;31;36mWelcome To");
print("\033[1;31;31m         dP   88                           IP'`Yb          ""\033[1;31;32m   Yb,  88      `8b                        IP'`Yb    ");
print("\033[1;31;31m        dP    88                           I8  8I          ""\033[1;31;32m    ``  88      ,8P                        I8  8I    ", "     \033[1;31;31mApple\033[1;31;32m Rush");
print("\033[1;31;31m       ,8'    88                           I8  8'          ""\033[1;31;32m        88aaaad8P`                         I8  8'    ", "     \033[0;31;32mRush To Collect the Apples to Survive Winter Time", "      \033[1;31;33mControls:");
print("\033[1;31;31m       d88888888   gg,gggg,    gg,gggg,    I8 dP   ,ggg,   ""\033[1;31;32m        88````Yb,    gg      gg    ,g,     I8 dPgg,  ", "     \033[0;31;32mAvoid Monsters And Be Careful With What you Get", "        \033[1;31;33mMove With WASD");
print("\033[1;31;31m __   ,8`     88   I8P`  `Yb   I8P`  `Yb   I8dP   i8` `8i  ""\033[1;31;32m        88     `8b   I8      8I   ,8'8,    I8dP` `8I ", "     \033[0;31;32mWhen Winter Time Comes You have to be near a Campfire", "  \033[0;31;33m W - Up");
print("\033[1;31;31mdP`  ,8P      Y8   I8'    ,8i  I8'    ,8i  I8P    I8, ,8I  ""\033[1;31;32m        88      `8i  I8,    ,8I  ,8'  Yb   I8P    I8 ", "     \033[0;31;32mOr Otherwise its Hard to Survive the harsh time", "        \033[0;31;33m A - Left");
print("\033[1;31;31mYb,_,dP       `8b,,I8 _  ,d8' ,I8 _  ,d8' ,d8b,_  `YbadP'  ""\033[1;31;32m        88       Yb,,d8b,  ,d8b,,8'_   8) ,d8     I8,", "     \033[0;31;32mYour Objective is to Survive A Week (7 Days)", "           \033[0;31;33m S - Down");
print("\033[1;31;31m `Y8P`         `Y8PI8 YY88888PPI8 YY88888P8P'`Y88888P`Y888 ""\033[1;31;32m        88        Y88P'`Y88P``Y8P' `YY8P8P88P     `Y8", "     \033[0;31;32mPress a Key to Start Good Luck" , "                         \033[0;31;33m D - Right");
print("\033[1;31;31m                   I8          I8");
print("\033[1;31;31m                   I8          I8");
print("\033[1;31;31m                   I8          I8");
print("\033[1;31;31m                   I8          I8");
print("\033[1;31;31m                   I8          I8");


Number = 2
Letter = 7


def UpdateRow(Number, Letter, Data):
    #Code Fix / Test
    #print(Season, "Update Row")
    global PreviousNumber
    if Season == "Spring":
        NewList = Dict2[Number]
        NewList = list(NewList)
        PreviousNumber = NewList[Letter]
        NewList[Letter] = Data
        #NewList[Letter + 1] = "🌳"
        NewList = "".join(NewList)
        Dict2.update({Number: NewList})
        UpdateScreen()
        for Counter2 in range(2, Difficulty, 1):
            print(Dict2[Counter2]); Row = ""

    if Season == "Winter":
        NewList = Dict2[Number]
        NewList = list(NewList)
        PreviousNumber = NewList[Letter]
        NewList[Letter] = Data
        NewList = "".join(NewList)
        Dict2.update({Number: NewList})
        UpdateScreen()
        for Counter2 in range(2, Difficulty, 1):
            print(Dict2[Counter2]);
            Row = ""

ListCheck = "hello"
def CheckList(Number, Letter):
    global ListCheck
    NewList = Dict2[Number]
    NewList = list(NewList)
    ListCheck = NewList[Letter]
    NewList = "".join(NewList)

CheckList(3, 5)
#print(ListCheck)

def AddCollectibles(Data):
    Number = randrange(1, 8)
    Letter = randrange(0, 9)
    UpdateRow(Number, Letter, Data)

CollectedApples = 0


#Player Movement


def UpdateGrid(Season):
    if Season == "Spring":
        Row = ""
        for Counter2 in range(0, Difficulty, 1):
            print(Dict2[Counter2]); Row = ""
            for Counter in range(0, Difficulty, 1):
                Emoji = randrange(0,7)
                Row = Row + Dict[Emoji]
            Dict2[(Counter2 + 1)] = Row
        print(Dict2[Counter2]);
        print(Dict2);


    if Season == "Winter":
        Row = ""
        for Counter2 in range(0, Difficulty, 1):
            #print(Dict2[Counter2]);
            Row = ""
            for Counter in range(0, Difficulty, 1):
                Emoji = randrange(0, 7)
                Row = Row + Dict4[Emoji]
            Dict2[(Counter2 + 1)] = Row
        #print(Dict2[Counter2]);
        #print(Dict2);



def MainLoop():
    global SeasonalTime; SeasonalTime = 0
    global Number;
    global Emoji
    global Season
    global Letter
    global CollectedApples; CollectedApples = 5
    global TotalCollectedApples
    global CurrentDay; CurrentDay = 1
    global PlayerHunger; PlayerHunger = 10
    while True:
        try:
            SeasonalTime = SeasonalTime + 0.01
            if Season == "Winter" and SeasonalTime >= 4.5:
                UpdateGrid("Spring")
                CurrentDay = CurrentDay + 1
                Season = "Spring"
                SeasonalTime = 0
                PlayerHunger = CollectedApples / 2.5
                CollectedApples = 0
                if CurrentDay == 7:
                    print(""); print("")
                    Colors("Yellow", "Bold")
                    ColorfulText("🎉🏆You Win You Have Survived🏆🎉")
                    Colors("Green", "Italic")
                    ColorfulText("You got home safely from this Adventurous Experience\033[00m\033[0;31;32m\nYou are shocked and yet relieved you are fine\n With a great memory and experience to share with your friends and relatives")
            if Season == "Spring" and SeasonalTime >= 4.5 and SeasonalTime <= 4.6:
                SeasonalTime = 0
                # Code Fix / Test
                #print("hello", SeasonalTime)
                PlayerHunger = CollectedApples / 2.5
                UpdateGrid("Winter")
                AddCollectibles("🔥")
                Season = "Winter"
                # Code Fix / Test
                #print(Season)

            # Player Movement
            if keyboard.is_pressed("w"):
                Number = Number - 1
                Emoji = randrange(0, 6)
                if Season == "Spring":
                    UpdateRow(Number + 1, Letter, Dict3[Emoji])
                    UpdateRow(Number, Letter, "🙂")
                if Season == "Winter":
                    UpdateRow(Number + 1, Letter, Dict4[Emoji])
                    UpdateRow(Number, Letter, "🙂")
                if Season == "Winter":
                    PlayerHunger = PlayerHunger - 0.15
                if PreviousNumber == "🍎":
                    CollectedApples = CollectedApples + 1
                    #TotalCollectedApples = TotalCollectedApples + 1
                if PlayerHunger < 0:
                    Colors("Red", "Bold")
                    ColorfulText("You Failed to survive")
                    Colors("Green", "Italic")
                    ColorfulText("You Were Found laying on the ground Starving\033[00m\033[0;31;32m\nYou have been hospitalized and now are ok\n With a bad memory of this tricky adventure")
                    exit()
                print("\033[1;31;33mDay", CurrentDay, "| 🍞 Hunger ", round(PlayerHunger)); print("\033[1;31;32mYou Have Collected", "🍎", CollectedApples, "\033[1;31;31mApples"); print(Season, SeasonalTime)
                time.sleep(0.4)


            if keyboard.is_pressed("s"):
                Number = Number + 1
                Emoji = randrange(0, 6)
                if Season == "Spring":
                    UpdateRow(Number - 1, Letter, Dict3[Emoji])
                    UpdateRow(Number, Letter, "🙂")
                if Season == "Winter":
                    UpdateRow(Number - 1, Letter, Dict4[Emoji])
                    UpdateRow(Number, Letter, "🙂")
                    PlayerHunger = PlayerHunger - 0.15
                if PreviousNumber == "🍎":
                    CollectedApples = CollectedApples + 1
                    #TotalCollectedApples = TotalCollectedApples + 1
                if PlayerHunger < 0:
                    Colors("Red", "Bold")
                    ColorfulText("You Failed to survive")
                    Colors("Green", "Italic")
                    ColorfulText("You Were Found laying on the ground Starving\033[00m\033[0;31;32m\nYou have been hospitalized and now are ok\n With a bad memory of this tricky adventure")
                    exit()
                print("\033[1;31;33mDay", CurrentDay, "| 🍞 Hunger ", round(PlayerHunger));
                print("\033[1;31;32mYou Have Collected", "🍎", CollectedApples, "\033[1;31;31mApples");
                time.sleep(0.4)

            if keyboard.is_pressed("a"):
                Letter = Letter - 1
                Emoji = randrange(0, 6)
                if Season == "Spring":
                    UpdateRow(Number, Letter + 1, Dict3[Emoji])
                    UpdateRow(Number, Letter, "🙂")
                if Season == "Winter":
                    UpdateRow(Number, Letter + 1, Dict4[Emoji])
                    UpdateRow(Number, Letter, "🙂")
                    PlayerHunger = PlayerHunger - 0.15
                if PreviousNumber == "🍎":
                    CollectedApples = CollectedApples + 1
                    #TotalCollectedApples = TotalCollectedApples + 1
                if PlayerHunger < 0:
                    Colors("Red", "Bold")
                    ColorfulText("You Failed to survive")
                    Colors("Green", "Italic")
                    ColorfulText("You Were Found laying on the ground Starving\033[00m\033[0;31;32m\nYou have been hospitalized and now are ok\n With a bad memory of this tricky adventure")
                    exit()
                print("\033[1;31;33mDay", CurrentDay, "| 🍞 Hunger ", round(PlayerHunger));
                print("\033[1;31;32mYou Have Collected", "🍎", CollectedApples, "\033[1;31;31mApples");
                time.sleep(0.4)

            if keyboard.is_pressed("d"):
                Letter = Letter + 1
                Emoji = randrange(0, 6)
                if Season == "Spring":
                    UpdateRow(Number, Letter - 1, Dict3[Emoji])
                    UpdateRow(Number, Letter, "🙂")
                if Season == "Winter":
                    UpdateRow(Number, Letter - 1, Dict4[Emoji])
                    UpdateRow(Number, Letter, "🙂")
                    PlayerHunger = PlayerHunger - 0.15
                if PreviousNumber == "🍎":
                    CollectedApples = CollectedApples + 1
                    #TotalCollectedApples = TotalCollectedApples + 1
                if PlayerHunger < 0:
                    Colors("Red", "Bold")
                    ColorfulText("You Failed to survive")
                    Colors("Green", "Italic")
                    ColorfulText("You Were Found laying on the ground Starving\033[00m\033[0;31;32m\nYou have been hospitalized and now are ok\n With a bad memory of this tricky adventure")
                    exit()
                print("\033[1;31;33mDay", CurrentDay, "| 🍞 Hunger ", round(PlayerHunger));
                print("\033[1;31;32mYou Have Collected", "🍎", CollectedApples, "\033[1;31;31mApples");
                time.sleep(0.4)
            time.sleep(0.01)
        except:
            print(SeasonalTime)
            break

MainLoop()


#UpdateRow(2, 4, "🙂")