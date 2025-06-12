# li = [10, 30, 32,48,56]
# def finder(a,b):
#     c = 0
#     for i in a:
#         if b == i:
#             print(c)
#             break
#         c=c+1

# finder(li,48)

li = [1,1,2,2,3,3,4,4,1,5,5,1,2,3,4,5,1,2,3,4,5]
linew = []
for i in li:
    if i in linew:
        continue
    else:
        linew.append(i)
        
print(linew)
print(li[1])
    
name = "Global IOT"
newname = ""
for i in name:
    if i == " ":
        newname = newname + "_"
    else:
        newname = newname + i

print(newname)