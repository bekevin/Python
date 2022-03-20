#Just a simple tip calculator
#Intro
print("Welcome to the tip calculator")

#ask for input
price = float(input("What was the toital bill?: "))
people = float(input("How many people to split the bill?: "))
tip = float(input("What percentage tip would you like to give?: "))

#math (price*tip)/people
total = round(float((price*(1+(tip/100)))/people),2)

#print total
print(f"Each person should pay: {total}")
