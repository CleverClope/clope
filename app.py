print("Hello world");

print("currency");
amount= float(input('enter amount'))
rate= float(input('rate of interest'))
years= int(input('Duration(number of years)?'))
total= (amount*pow(1+(rate/100),years))
interest= total-amount
print('/n Interest=%0.2f'%interest)


