enter_number = int(input("number: "))
prime = True
for i in range(2,enter_number-1):
    if enter_number%i == 0:
        prime = False
        break
if not prime:
    print("not prime")
else:
    print("prime number")