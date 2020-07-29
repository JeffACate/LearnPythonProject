tot = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        line = line.strip()
        start = line.find('0')
        end = len(line)
        section = line[start:end]
        num = float(section)
        tot = num + tot
        count = count + 1
print("Average spam confidence: ", tot/count)

