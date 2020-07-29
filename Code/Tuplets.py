name = input("Enter file:")
if len(name) < 1 : name = "files/mbox-short.txt"
handle = open(name)
dates = list()
counts = dict()
months = list()
for line in handle:
    if line.startswith('From '):
        month = line.split(':')
        dates.append(month[0])
for date in dates:
    start = len(date) - 2
    end = len(date)
    month = date[start:end]
    months.append(month)
    if month in counts.keys():
        counts[month] = counts[month] + 1
    else:
        counts.update({month:1})
months.sort()
counts = sorted(counts.items())
for item in counts: print(item[0], item[1])