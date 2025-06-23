li1 = [1,34232,32,345,345,3454,346546,898679,65765,8,65678,68,768568,658687]
high_num = max(li1)
print(high_num)
new_li2 = sorted(li1)
print(new_li2[-2])

second_highest = 0
for i in li1:
    if i > second_highest and i < high_num:
        second_highest = i
print(second_highest)