num = int(input("enter your destiny number: "))
a = 0
b = 1
if num == 1:
    print(a)
elif num == 2:
    print(a)
    print(b)
elif num > 2:
    print(a)
    print(b)
    for i in range(num-2):
        c = a + b
        print(c)
        a = b
        b = c
else:
    print("invalid input") 
