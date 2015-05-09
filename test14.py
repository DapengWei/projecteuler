max = 0
for i in xrange(1,1000000):
    j = 0
    k = i
    while k > 1:
        j = j+1
        if j > max:
            max = j
            max_num = i
        if k%2 == 0:
            k = k / 2
        else:
            k = k*3 +1
print max_num,max