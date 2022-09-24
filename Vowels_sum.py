

word = input()
s = 0

for x in range(0, len(word)):
    if word[x] == "a":
        s = s + 1
    if word[x] == "e":
        s = s + 2
    if word[x] == "i":
        s = s + 3
    if word[x] == "o":
        s = s + 4
    if word[x] == "u":
        s = s + 5
print(s)
