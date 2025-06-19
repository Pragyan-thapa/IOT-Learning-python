# msg = "hello welcome to globalIOT"
# print(msg)
# find_char = input("enter a character from above sentence to find its index: ")

# def finding_index(sent,char):
#     count = 0
#     for i in sent:
#         if i == char:
#             break
#         else:
#             count += 1
#     return(count)

# index_count = finding_index(msg,find_char)
# print("index of the character in above sentence is: ",index_count)

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
