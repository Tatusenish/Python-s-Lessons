my_file = open("text2.txt", "r", encoding="utf-8")
lines = 0
words = 0
for line in my_file:
    wordlist = line.split()
    lines += 1
    words = len(wordlist)
    print("Number of words in line is: ", words)
    words += 1
print("Number of lines is: ", lines)
my_file.close()




