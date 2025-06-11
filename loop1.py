# i = 1
# while i < 10:
#     print(i)
#     i = i + 2

# n = int(input("enter your prefered number: "))
# i = 2
# while i <=n:
#     print(i)
#     i+=2

# i = 9
# while i>0:
#     print(i)
#     i-=2

# n = int(input("enter your destiny number: "))
# i = 1
# sum = 0
# while i<=n:
#     sum = sum + i
#     i = i + 1
# print("total is: ",sum)

# n = int(input("enter your number for multiplication: "))
# i = 1
# while i < 11:
#     m = n*i
#     print(f"{n} * {i} = {m}")
#     i +=1

# for i in range(10,1,-2):
#      print(i)
     
# NOT COMPLETE
# li1=[[1,2,3],[4,5,6],[6,5,8]]
# li2=[[6,7,3],[5,7,2],[6,3,8]]
# newlist = []
# for i in range(len(li1[0])):
#     for j in range(len(li2[0])):
#         sum = li1[i][j]+li2[i][j]
#         newlist = [sum]
# print(newlist)

# li1 = [1,2,3,4,5]
# total = 0
# for i in li1:
#     total = total + i
# print(total)
# li1.reverse()
# print(li1)

# for i in range(1,2):
#     for j in range(1,6):
#         print(f"{j}"*5)

outs = ""
for i in range(1,2):
    for j in range(1,6):
        outs = outs+str(j)
        print(outs)

