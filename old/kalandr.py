import math

r1 = 0.05
r2 = 0.06

log = math.log(math.log(r2/r1))

T = 100 - (40 * (100 - 20)) / ( (50/r2) + 40 * log ) * log

print(T)


import math

l = 5
F = 20
p = 10

w1 = int((math.pi / l) * math.sqrt(F/(p * (pow(10, -5)))) * pow(10, 1))
w2 = 2 * w1
w3 = 3 * w1

print(w1)


# 0.62 * 