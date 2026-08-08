import pandas as pd

temperatures = [35, 25, 26, 25, 29, 27, 38]
avg =  sum(temperatures)/len(temperatures)

def announce():
    for day, temp in enumerate(temperatures):
        print(f"วันที่ {day+1} มีค่า {temp} องศา")

def classify_temp(t, avg):
    if t>avg:
        return "ร้อน"
    else: 
        return "เย็น"

announce()
print(classify_temp(30, avg))

df = pd.read_csv("pokemon.csv")
print(df.head())