fname = input('Enter file name: ')

if len(fname) < 5 : fname = 'files\mbox-short.txt'
fh = open(fname)
addresses = {}
for line in fh:
    if line.startswith('From '):
        address = line.split()[1]
        if address in addresses.keys():
            addresses[address] = addresses[address] + 1
        else:
            addresses.update({address:1})
for address in addresses:
    if addresses[address] == max(addresses.values()):
        print(address, addresses[address])