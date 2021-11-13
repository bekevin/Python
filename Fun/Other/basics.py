import time
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(type(data))
        print(data.mean()["st1"])
        
    else:
        print("File does not exist.")
    time.sleep(3)
    
