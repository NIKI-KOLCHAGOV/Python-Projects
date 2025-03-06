class Colors:
  def __init__(self, color, effect):
    self.color1 = color
    self.TextEffect = effect
    global ChoosenColor
    global ChoosenTextEffect
    ChoosenColor = color
    ChoosenTextEffect = effect

ClearColors = "False"

def ClearColor():
    global ClearColors
    ClearColors = "True"

ColorsList = ["Red", "Green", "Blue", "Yellow", "Purple", "Cyan", "Gray", "Black", "Rainbow"]
EffectsList = ["Regular", "Bold", "Italic", "Underline"]

def ColorfulText(Text):
    if ClearColors == "True":
        print(Text)
        exit()
    if (ChoosenColor in ColorsList) == True:
        if (ChoosenTextEffect in EffectsList) == True:
            if ChoosenTextEffect == "Bold":
                if ChoosenColor == "Red":
                    JoinTextAndColor = "\033[1;31;31m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Green":
                    JoinTextAndColor = "\033[1;31;32m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Yellow":
                    JoinTextAndColor = "\033[1;31;33m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Blue":
                    JoinTextAndColor = "\033[1;31;34m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Purple":
                    JoinTextAndColor = "\033[1;31;35m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Cyan":
                    JoinTextAndColor = "\033[1;31;36m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Gray":
                    JoinTextAndColor = "\033[1;31;37m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Black":
                    JoinTextAndColor = "\033[1;31;38m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Rainbow":
                    ColorFormatList = ["\033[1;31;31m", "\033[1;31;32m", "\033[1;31;33m", "\033[1;31;34m", "\033[1;31;35m", "\033[1;31;36m"]
                    JoinTextAndColor = ""
                    Counter3 = 0
                    for Counter2 in range(0, (len(Text) // 6) + 1, 1):
                        for Counter in range(0, 5, 1):
                            JoinTextAndColor = JoinTextAndColor + ColorFormatList[Counter] + Text[Counter3 + Counter]
                        Counter3 = Counter3 + 5
                    print(JoinTextAndColor)

            if ChoosenTextEffect == "Regular":
                if ChoosenColor == "Red":
                    JoinTextAndColor = "\033[0;31;31m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Green":
                    JoinTextAndColor = "\033[0;31;32m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Yellow":
                    JoinTextAndColor = "\033[0;31;33m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Blue":
                    JoinTextAndColor = "\033[0;31;34m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Purple":
                    JoinTextAndColor = "\033[0;31;35m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Cyan":
                    JoinTextAndColor = "\033[0;31;36m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Gray":
                    JoinTextAndColor = "\033[0;31;37m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Black":
                    JoinTextAndColor = "\033[0;31;38m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Rainbow":
                    ColorFormatList = ["\033[0;31;31m", "\033[0;31;32m", "\033[0;31;33m", "\033[0;31;34m", "\033[0;31;35m", "\033[0;31;36m"]
                    JoinTextAndColor = ""
                    Counter3 = 0
                    for Counter2 in range(0, (len(Text) // 6) + 1, 1):
                        for Counter in range(0, 5, 1):
                            JoinTextAndColor = JoinTextAndColor + ColorFormatList[Counter] + Text[Counter3 + Counter]
                        Counter3 = Counter3 + 5
                    print(JoinTextAndColor)

            if ChoosenTextEffect == "Italic":
                if ChoosenColor == "Red":
                    JoinTextAndColor = "\033[3;31;31m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Green":
                    JoinTextAndColor = "\033[3;31;32m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Yellow":
                    JoinTextAndColor = "\033[3;31;33m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Blue":
                    JoinTextAndColor = "\033[3;31;34m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Purple":
                    JoinTextAndColor = "\033[3;31;35m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Cyan":
                    JoinTextAndColor = "\033[3;31;36m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Gray":
                    JoinTextAndColor = "\033[3;31;37m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Black":
                    JoinTextAndColor = "\033[3;31;38m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Rainbow":
                    ColorFormatList = ["\033[3;31;31m", "\033[3;31;32m", "\033[3;31;33m", "\033[3;31;34m", "\033[3;31;35m", "\033[3;31;36m"]
                    JoinTextAndColor = ""
                    Counter3 = 0
                    for Counter2 in range(0, (len(Text) // 6) + 1, 1):
                        for Counter in range(0, 5, 1):
                            JoinTextAndColor = JoinTextAndColor + ColorFormatList[Counter] + Text[Counter3 + Counter]
                        Counter3 = Counter3 + 5
                    print(JoinTextAndColor)

            if ChoosenTextEffect == "Underline":
                if ChoosenColor == "Red":
                    JoinTextAndColor = "\033[4;31;31m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Green":
                    JoinTextAndColor = "\033[4;31;32m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Yellow":
                    JoinTextAndColor = "\033[4;31;33m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Blue":
                    JoinTextAndColor = "\033[4;31;34m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Purple":
                    JoinTextAndColor = "\033[4;31;35m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Cyan":
                    JoinTextAndColor = "\033[4;31;36m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Gray":
                    JoinTextAndColor = "\033[4;31;37m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Black":
                    JoinTextAndColor = "\033[4;31;38m" + Text
                    print(JoinTextAndColor)
                if ChoosenColor == "Rainbow":
                    ColorFormatList = ["\033[4;31;31m", "\033[4;31;32m", "\033[4;31;33m", "\033[4;31;34m", "\033[4;31;35m", "\033[4;31;36m"]
                    JoinTextAndColor = ""
                    Counter3 = 0
                    for Counter2 in range(0, (len(Text) // 6) + 1, 1):
                        for Counter in range(0, 5, 1):
                            JoinTextAndColor = JoinTextAndColor + ColorFormatList[Counter] + Text[Counter3 + Counter]
                        Counter3 = Counter3 + 5
                    print(JoinTextAndColor)
        else:
            print("\033[1;31;31mError: Text Effect Not Found")
    else:
        print("\033[1;31;31mError: Color Not Found")



#Colors("Red", "Regular")
#ColorfulText("Test")

#def Colors(Color):
#    print("\033[1;31;31m", "Hello")
#Colors("Red")
