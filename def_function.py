def hello(to="world"):
    print("hello",to)
name= input("Enter Your Name: ")
if name:
    hello(name)
else:
    hello()
