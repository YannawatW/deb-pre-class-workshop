sales = [120, 340, 560, 80, 999]
total = sum(sales)
average = total / len(sales)


def classify(value, avg):
    return "สูง" if value > avg else "ต่ำ"


print(classify(300, average))

