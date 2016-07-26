convert = int(raw_input('Please enter a number.\n'))

counter = 0
while convert >= 1:
    convert = convert / 10
    counter += 1

print counter