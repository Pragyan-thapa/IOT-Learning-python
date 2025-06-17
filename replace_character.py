word = "globalIOT"
print(word[3])
to_replace = 'l'
replacing_character = 'a'
new_word = ""
for i in word:
    if i == to_replace:
        new_word += replacing_character
    else:
        new_word = new_word + i

print(new_word)