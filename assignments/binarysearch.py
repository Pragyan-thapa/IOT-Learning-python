the_pond = [3,6,4,8,9,1,4,2,1,6,7,8,9]
name_pond = ["milan","suman","nishan","abishek","rita","gita","punam","roshan","manoj"]
set_the_pond = set(the_pond)
# print(the_pond,set_the_pond)
# li = sorted(set_the_pond)
# print(li[len(li)//2])
# new_pond = li[:len(li)//2]
# print(new_pond)

def bi_search(pond,tofind):
    if tofind == pond[0]:
        msg = "found"
        return msg
    elif tofind > pond[len(pond)-1]:
        msg = "no number"
        return msg
    elif tofind < pond[0]:
        msg = "no number"
        return msg
    elif tofind == pond[len(pond)//2]:
        msg ="there is number"
        return msg
    elif tofind > pond[len(pond)//2]:
        abc = pond[len(pond)//2:]
        print(abc)
        return bi_search(abc,tofind)
    elif tofind < pond[len(pond)//2]:
        abc = pond[:len(pond)//2]
        print(abc)
        return bi_search(abc,tofind)
    
    
    
# user_tofind = int(input("enter the number: "))
# print(bi_search(li,user_tofind))

b = sorted(name_pond)
print(b)
nam = input("enter name to check: ")

print(bi_search(b,nam))
