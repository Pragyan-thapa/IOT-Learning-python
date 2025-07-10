score = int(input("enter your score on 100: "))
salary = 150000

if score > 80:
    bonus = 0.3 * salary
elif score >60 and score < 80:
    bonus = 0.2 * salary
elif score <60:
    bonus = 0.1 * salary

print("enter your bonus is: ",bonus)