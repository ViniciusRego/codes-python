string = input()
first = input()
last = input()
word = str()
for i in string:
    if i == first or i != first:
        if i == first:
            word += last
        else:
            word += i

print(word)