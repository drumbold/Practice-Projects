# Roman numeral converter. Asks the user for a number and then
# converts the number to it's roman numeral
import collections

convert = int(raw_input('Please enter a number.\n'))

# # Counters that correspond with their roman numeral value
# M = 0
# CM = 0
# D = 0
# CD = 0
# C = 0
# XC = 0
# L = 0
# XL = 0
# X = 0
# IX = 0
# V = 0
# IV = 0
# I = 0

# # Looping if statement to determine the number and add to the counters
# while convert > 0:
#     if convert >= 1000:
#         convert = convert - 1000
#         M += 1
#     elif convert >= 900:
#         convert = convert - 900
#         CM += 1
#     elif convert >= 500:
#         convert = convert - 500
#         D += 1
#     elif convert >= 400:
#         convert = convert - 400
#         CD += 1
#     elif convert >= 100:
#         convert = convert - 100
#         C += 1
#     elif convert >= 90:
#         convert = convert - 90
#         XC += 1
#     elif convert >= 50:
#         convert = convert - 50
#         L += 1
#     elif convert >= 40:
#         convert = convert - 40
#         XL += 1
#     elif convert >= 10:
#         convert = convert - 10
#         X += 1
#     elif convert >= 9:
#         convert = convert - 9
#         IX += 1
#     elif convert >= 5:
#         convert = convert - 5
#         V += 1
#     elif convert >= 4:
#         convert = convert - 4
#         IV += 1
#     else:
#         convert = convert - 1
#         I += 1

# print "M" * M + "CM" * CM + "D" * D + "CD" * CD + "C" * C + "XC" * XC + "L" * L + "XL" * XL + "X" * X + "IX" * IX + "V" * V + "IV" * IV + "I" * I

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


for key, value in numerals.items():
    divider = convert / value
    if divider > 0:
        print(divider) * key,
        convert = convert % value
    else:
        continue