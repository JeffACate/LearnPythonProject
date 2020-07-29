largest = None
smallest = None
notDone = True
while notDone:
    num = input("Enter a number: ")
    print(num)
    if num == 'done':
        print("done")
        notDone = False
        break
    try:
        num = float(num)
        print(num)
    except:
        print("Invalid input")
        continue
    if largest == None:
        largest = num
    if smallest == None:
        smallest = num
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

	

print("Maximum", largest)
print("Minimum", smallest)