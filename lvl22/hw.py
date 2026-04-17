# 1
name = "Sandro"
print(name[0])

# 2
surname = "Pipia"
print(surname[-1])

# 3
word = "Python"
print(word[2])

# 4
word = "Programming"
print(word[:4])

# 5
word = "Computer"
print(word[-3:])

# 6
word = "HelloWorld"
print(word[3:7])  # loWo

# 7
word = "Georgia"
print(word[2:6])

# 8
word = "Apple"
if word[0] == "A":
    print(word[:3])
else:
    print(word[-3:])

# 9
word = "Education"
print(word[1:-1])

# 10
word = "Developer"
new_word = word[:3] + word[-3:]
print(new_word)

# 11
sentence = "Hello my friend"
print(sentence[:sentence.find(" ")])

# 12
word = "abcdef"
print(word[::2])

# 13
lst = [1, "a", True, 5.5, "hello", False, 9, "x"]
print(lst[2:6])

# 14
musicians = ["Drake", "Travis", "Kanye", "Future", "Metro", "21Savage"]
print(musicians[-2:])