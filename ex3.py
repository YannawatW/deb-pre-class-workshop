sales = [120, 340, 560, 80, 999]
total = sum(sales)
average = total / len(sales)

for i, s in enumerate(sales):
    if s > average:
        print(f"รายการที่ {i} สูงกว่าค่าเฉลี่ย: {s}")
