import pandas as pd

data = pd.read_excel(here has to be the file path to your excel file, decimal = ";")

n = float(data["time"].iloc[-1])#takes the newest data in the column time
f = float(data["time"].min())#takes the fastest lap
fastest_lap= data.loc[data["time"].idxmin()]#takes the whole line with the fastest time
print(fastest_lap)#shows the line with the fastest time

d = n - f
print("Delta time between newest and fastest time: ", d)#shows the delta time

#Important----------------------
#Your excel file has to include a column which calls "time"
#You can change it but then you have to do it in the Excel file AND in the Code