for i in xrange(1,1000):
    for j in xrange(i+1,1000):
        k = 1000 - i - j
        if i*i+j*j == k*k: 
            print i*j*k