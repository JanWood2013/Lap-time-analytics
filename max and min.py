import pandas as pd #python library
import matplotlib.pyplot as plt #python library
data = pd.read_excel(Here the file path to the excel file With your data, decimal=",") #reads the excel file and creates a dataFrame
print(data) #shows the DataFrame 
print("-min", data.loc[data["Zeit"].idxmax()]) #min. time
print() #only design
print("max", data.loc[data["Zeit"].idxmin()]) #max. time
print() #only design
print("Durchschnitt:", sum(data["Zeit"])/len(data["Zeit"])) #time average
plt.scatter(data["Runde"], data["Zeit"]) #shows the lap times with points
plt.plot(data["Runde"], data["Zeit"], color = "red" ) #showsthe line between the times in red
plt.show() #shows the diagramm


#   Important command:
#   example.loc[x["z"].idxmax/min] calculates max and/or min and shows the whole line where the data is (like also the lap)