# char = input("enter the character: ")
# low_char = char.lower()
# list_char = list(low_char)
# dict_char = {list_char[i]:list_char.count(list_char[i]) for i in range(len(list_char))}
# print(dict_char)
# dict_val = dict_char.values()
# max_val = max(dict_val)
# for a,b in dict_char.items():
#     if b == max_val:
#         print(f"most frequently used word is {a}")


# inverted_dict = {}
# for x,y in dict_char.items():
#     inverted_dict[y] = x
# print(inverted_dict)



# words = "aaabbcccddsssaaffggkkjjhh"
# words_set = sorted(set(words))
# words_list = sorted(list(words))
# compressed_word = ""

# for i in words_set:
#     count = words_list.count(i)
#     compressed_word = compressed_word + i + str(count)

# print(compressed_word)

# li1 = [0,2,1,4,3,6,4,9,6,7,0,8]
# for a in li1:
#     if a == 0:
#         li1.remove(a)
#         li1.append(a)
    
# print(li1)

d1 = {"a": 10, "b": 5}
d2 = {"a": 3, "c": 8}
d3 = {}
for x,y in d1.items():
    new_val = 0
    for j,k in d2.items():
        if x == j:
            new_val = y + k
            d3[x]=new_val
        elif j not in d3:
            d3[x]=y
            d3[j]=k
print(d3)