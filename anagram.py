
list = ["232", "mishka", "121", "muha"]
new_list = []

for w in list:
    new_list.append(w)

print(new_list)
for word in new_list:
    rev_word = word[::-1]
    if rev_word == word:
        print("Yes")
    else:
        print("No") 

