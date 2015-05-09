numfile = open("test8.txt","r")
num_str = numfile.read()
numx_list = []
for i in xrange(1000-4):
    sum = 1
    for j in xrange(5):
        sum = sum*int(num_str[i+j])
    numx_list.append(sum)
print max(numx_list)