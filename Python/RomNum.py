# Roman numeral converter. Asks the user for a number and then
# converts the number to it's roman numeral
import collections

convert = int(raw_input('Please enter a number.\n'))

# Considering and trying to implement a dictionry
numerals = collections.OrderedDict()
numerals["M"] = 1000
numerals["CM"] = 900
numerals["D"] = 500
numerals["CD"] = 400
numerals["C"]  = 100
numerals["XC"] = 90
numerals["L"] = 50
numerals["XL"] = 40
numerals["X"] = 10
numerals["IX"] = 9
numerals["V"] = 5
numerals["IV"] = 4
numerals["I"] = 1

out = ""
for key, value in numerals.items():
    divider = int(convert / value)
    out += (divider) * key
    convert = convert % value
print out