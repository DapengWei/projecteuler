import math
i = 2
j = 1

def prime_detect(num):
    for x in xrange(2,int(math.ceil(math.sqrt(float(num))+1))):
        if num%x == 0:
            return False
    return True
while j <= 10001:
    if prime_detect(i) or i == 2:
        j = j+1
    i = i+1

print i-1