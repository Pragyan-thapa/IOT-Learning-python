# def facto(n):
#     if n == 1:
#         return(1)
#     else:
#         return(n * facto(n-1))

# print(facto(3))


# def fibbonaci(n):
#     if n <= 1:
#         return(1)
#     else:
#         return(fibbonaci(n-1)+fibbonaci(n-2))
    
# for i in range(10):
#     print(fibbonaci(i))

lis1 = [1,2,3,4,5]
new_li = []
def subsets(h):
    g = h.copy()
    if len(h) == 1:
        i=[]
        new_li.append(h)
        new_li.append(i)
        sorted_list = sorted(new_li, key=len)
        return(sorted_list)
    else:
        new_li.append(g)
        element = [h.pop()]
        new_li.append(element)
        return(subsets(h))

print(subsets(lis1))
# subsets(lis1)

# print(new_li)

# list1 = [1,2,3,4,4,5,66,6,7,8,8,9]

# list1.pop()
# print(list1)
