
import pandas as pd
import numpy as np

#Transformamos los datos de .arff a .csv
path = ""
f = open(path+"cpu.arff")
lines = f.read().splitlines()
header = []
data = []
types = []
b = False
for line in lines:
    if("@attribute" in line):
        atr = line.split(" ")
        header.append(atr[1])
        types.append(atr[2])
    if(b):
        dt = line.split(",")
        data.append(dt)
    if("@data" in line):
        b = True
    
for dat in data:
    for i in range(len(dat)):
        if(types[i] == "numeric"):
            dat[i] = int(dat[i])

data = np.array(data)
df = pd.DataFrame(data)
df.columns = header
df.to_csv(path+"cpu.csv", index = False, header = True)


#leemos el archivo csv para verificar que se haya guardado satifacotriamnete

csvFile = pd.read_csv(path+"cpu.csv")
print(csvFile)
