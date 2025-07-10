# set1 = {20,"suman",24,25}
# print({"suman"}.issubset(set1))

# se1 = {1,2,3,4,5}
# se2 = {4,5,6,7,8}


# print(se1 | se2) 
# print(se1 & se2)
# print(se1.difference(se2))
# print(se1.symmetric_difference(se2))

# square_set = {a*a for a in range(1,11) }
# print(square_set)
# hash()

se1 = {1,2,3,4,5}
se2 = {1,2,3}

print(se2.issubset(se1))
print(se1.issuperset(se2))