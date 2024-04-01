print("What is the weather forecast for tomorrow?")
temperature = int(input("What will be the temperature in Celsius: "))
rain = input("Will it rain? (yes/no): ")

if temperature >= 20:
    if rain == 'yes':
        print("Wear a dark-colored shirt/blouse and trousers or a skirt!")
        print("Don't forget to carry an umbrella and wear your boots!")
    else:
        print("Wear a light shirt/blouse/t-shirt and light material trousers/shorts or a skirt!")
    print("Have yourself a lovely day ahead!")

elif temperature == 10:
    if rain == 'yes':
        print("Wear warm clothes and don't forget your coat!")
        print("Don't forget to carry an umbrella and wear your boots!")
    else:
        print("Wear warm clothes and don't forget your coat!")
    print("Have yourself a lovely day ahead!")

elif temperature <= 5:
    if rain == 'yes':
        print("Wear a very heavy jumper, a full neck, some warm socks, and gloves!")
        print("Don't forget to carry an umbrella and wear your boots!")
        print("Sssssshhhh it's going to be a cold day!!")
    else:
        print("Wear a very heavy jumper, a full neck, some warm socks, and gloves!")
        print("Sssssshhhh it's going to be a cold day!!")
    print("Have yourself a lovely day ahead!")

else:
    print("The temperature is moderate. Dress comfortably and enjoy your day!")
