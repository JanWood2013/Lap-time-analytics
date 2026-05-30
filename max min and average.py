import pandas as pd #python library
import matplotlib.pyplot as plt #python library
data = pd.read_excel(Here the file path to the excel file With your data, decimal=",") #reads the excel file and creates a dataFrame
print(data) #shows the DataFrame 
print("-min", data.loc[data["time"].idxmax()]) #min. time
print() #only design
print("max", data.loc[data["time"].idxmin()]) #max. time
print() #only design
print("Durchschnitt:", sum(data["time"])/len(data["time"])) #time average
plt.scatter(data["laps"], data["time"]) #shows the lap times with points
plt.plot(data["laps"], data["time"], color = "red" ) #showsthe line between the times in red
plt.show() #shows the diagramm



#---------------------------------------------------------------------
#THE TIME IN YOUR EXCEL FILE HAS TO BE IN A COLUMN WHICH CALLS TIME
#---------------------------------------------------------------------
#THE LAPS HAVE TO BE IN A COLLUM WHICH CALLS LAPS
#---------------------------------------------------------------------
#if you dont want it like this you have to change it in the code but everywhere in the code
#   Important command:
#   example.loc[x["z"].idxmax/min] calculates max and/or min and shows the whole line where the data is (like also the lap)