temp = float(input("enter the Temperature: "))
hum = float(input("enter the humidity: "))

if temp >= 30 and hum>=90:
    print("Weather is Hot and Humid")
elif temp>=30 and hum<90:
    print("Weather is Hot")
elif temp<30 and hum>=90:
    print("Weather is Cold and Humid")
elif temp<30 and hum<90:
    print("weather is cold")
