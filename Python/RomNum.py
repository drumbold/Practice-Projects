convert = int(raw_input('Please enter a number.\n'))

# counter = 0
# while convert >= 1:
#     convert = convert / 10
#     counter += 1

# print counter

M = 0
D = 0
C = 0
L = 0
X = 0
V = 0
I = 0

while convert > 0:
    if convert >= 1000:
        convert = convert - 1000
        M += 1
    elif convert >= 500:
        convert = convert - 500
        D += 1
    elif convert >= 100:
        convert = convert - 100
        C += 1
    elif convert >= 50:
        convert = convert - 50
        L += 1
    elif convert >= 10:
        convert = convert - 10
        X += 1
    elif convert >= 5:
        convert = convert - 5
        V += 1
    else:
        convert = convert - 1
        I += 1

print M, D, C, L, X, V, I