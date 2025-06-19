name_1 = input("Please enter the word to check if palindrom: ")
loop_count = len(name_1)//2
end = -1
start = 0
palindrom = False

while start != (loop_count+1):
    if name_1[start] == name_1[end]: 
        end = end-1
        start +=1
        palindrom = True
    else:
        palindrom = False
        break
print(palindrom)
