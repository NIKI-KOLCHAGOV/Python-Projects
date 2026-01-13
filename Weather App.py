import requests, json
#from kaspersmicrobit import KaspersMicrobit
#from kaspersmicrobit import microbit_connection
import time

APIKey = "b062d6b21d88edade3c0e7994055fc90"

BaseUrl = "https://api.openweathermap.org/data/2.5/weather?"
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

City = "Bansko"; CountryCode = "bg"

Address1 = "E3:7E:99:0D:C1:BA"
Address2 = "E3:7E:99:0D:C1:BA"

#mb1 = microbit_connection(Address1)
#mb2 = microbit_connection(Address2)
#mb1 = KaspersMicrobit('E3:7E:99:0D:C1:BA')
#mb2 = KaspersMicrobit('C3:7F:94:0C:B1:BA')
#mb1.connect()
#mb2.connect()

#mb1.uart.send_string("First\n")
#mb2.uart.send_string("Second\n")

CompleteUrl = BaseUrl + "q=" + City + "," + CountryCode + "&appid=" + APIKey

while True:
    response = requests.get(CompleteUrl)
    print(CompleteUrl)
    jsonresult = response.json()
    if jsonresult["cod"] == 200:
        print("\033[1;32mSuccess: \033[0;32mRequest Successfully Recieved - " + str(jsonresult["cod"]) + "\033[0;00m")
    else:
        print("\033[0;31mError Request Failed - " + str(jsonresult["cod"]) + "\033[0;00m")
        quit(print(jsonresult["message"]))

    print(jsonresult)
    Send = jsonresult["weather"]; Send = Send[0]; Send = str(Send["id"]) + "," + Send["icon"] + ","
    Send2 = jsonresult["main"]; Send3 = str(Send2["temp"]) + "," + str(Send2["feels_like"]) + "," + str(Send2["pressure"]) + "," + str(Send2["humidity"])
    Send2 = jsonresult["visibility"]; Send3 = Send3 + "," + str(Send2)
    Send2 = jsonresult["wind"]; Send3 = Send3 + "," + str(Send2["speed"])
    Send2 = jsonresult["clouds"]
    Send3 = Send + Send3 + "," + str(Send2["all"])
    print("\033[0;37mSending: " + Send3)
    #mb1.uart.send_string("First\n")
    #mb2.uart.send_string("Second\n")
    time.sleep(300)

mb1.disconnect()
mb2.disconnect()


