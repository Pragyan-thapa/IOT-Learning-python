electricity_unit= int(input("enter you electricity unit: "))
bill = 0
if electricity_unit <= 100:
    bill = 0
    total_bill = bill
elif electricity_unit > 100 & electricity_unit <= 200:
  new_bill = bill - 100
  bill = new_bill * 5
  total_bill = bill
elif electricity_unit > 200 & electricity_unit <=300:
   new_bill = bill - 200
   bill = new_bill * 7
   total_bill = (100*5) + bill
total_bill = (100*5)+ (100*7)+((electricity_unit-300) * 10)
 

print(total_bill)