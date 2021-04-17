hours = input('Enter hours: ')
rate = input('Enter rate: ')
pay = float(hours) * float(rate)
if pay > 12:
    print(pay)
if pay < 12:
    print(float(pay) * 5)
