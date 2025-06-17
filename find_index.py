msg = "hello welcome to globalIOT"
print(msg)
find_char = input("enter a character from above sentence to find its index: ")

def finding_index(sent,char):
    count = 0
    for i in sent:
        if i == char:
            break
        else:
            count += 1
    return(count)

index_count = finding_index(msg,find_char)
print("index of the character in above sentence is: ",index_count)