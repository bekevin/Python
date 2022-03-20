#how many time until you die at 90?
age = int(input("what is your current age? "))

years = 90-age
days = years*365
weeks= years*52
months = years*12

message=f"you have {days} days, {weeks} weeks, and {months}, months left."

print(message)