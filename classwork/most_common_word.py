sentence = input("enter sentence: ")

def word_count(sentn):
    w_cont = 1
    for i in sentn:
        if i == " ":
            w_cont += 1
    return(w_cont)


def finding_uniques(lit):
    unique_list = []
    for i in lit:
        if i not in unique_list:
            unique_list.append(i)
    return(unique_list)


number_of_words = word_count(sentence)
list_words = []
x = 0
for i in range(number_of_words):
    word = ""
    for j in sentence[x:]:
        if j == " ":
            x += 1
            break
        else:
            word += j
            x +=1
    list_words.append(word)
print(list_words)
uni1 = finding_uniques(list_words)
print(uni1)

counting = []
for most in range(len(uni1)):
    first_index_count = list_words.count(uni1[most])
    counting.append(first_index_count)        

print(counting)

max_index = counting.index(max(counting))

print("most common word is ",uni1[max_index])
