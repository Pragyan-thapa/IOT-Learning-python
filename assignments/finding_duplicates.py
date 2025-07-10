l1 = [1,1,2,2,3,3,4,5,6,6,7,1,4,6]

# def find_duplicate(d1):
#     duplicates = []
#     c=1
#     for i in d1:
#         for j in d1[c:]:
#             if i == j and i not in duplicates:
#                 duplicates.append(i)
#                 break
#         c = c+1
#     return(duplicates)

# print(find_duplicate(l1))

def duplicates(listeer):
    seen = set()
    dups = set()
    for item in listeer:
        if item in seen:
            dups.add(item)
        else:
            seen.add(item)
    print(seen)
    return(dups)
print(duplicates(l1))