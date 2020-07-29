fname = input("Enter file name: ")
# pylint: disable=fixme, anomalous-backslash-in-string 
if len(fname) < 1 : fname = "files\mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

for line in fh:
    if line.startswith('From '):
        count = count + 1
        foundAddress = line.split()[1]
        lst.append(foundAddress)
for address in lst:
    print(address)
print("There were", count, "lines in the file with From as the first word")