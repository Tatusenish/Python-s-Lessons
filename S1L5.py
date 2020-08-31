my_file = open("text.txt", "a+", encoding="utf-8")
my_file.write("Phython\nPhython\nPhython\n")
my_file.seek(0)
for i in my_file:
    print(i, end="")
my_file.close()