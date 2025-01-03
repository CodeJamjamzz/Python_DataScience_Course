import pandas as pnd 

dict = {
    "countries": ["philippines", "japan", "korea", "china", "thailand"],
    "population": ["100M", "200M", "300M", "400M", "500M"],
    "capital": ["manila", "tokyo", "seoul", "beijing", "bangkok"]
}

dataFrame = pnd.DataFrame(dict)

dataFrame.index = ["PH", "JP", "KR", "CN", "TH"]
print(dataFrame)
    
try:
    csvData = pnd.read_csv("data.csv", index_col=0)
    print(csvData)
except FileNotFoundError:
    print("The file 'data.csv' was not found.")

