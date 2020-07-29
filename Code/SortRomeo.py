fname = input("Enter file name: ")
if len(fname) < 1 : fname = "files/romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)

lst.sort()
print(lst)