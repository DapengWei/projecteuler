numfile = open("test11.txt","r")
num_str = numfile.readlines()
for i in xrange(len(num_str)):
    num_str[i] = num_str[i].strip("\n")
    num_str[i] = num_str[i].split(" ")
    for j in xrange(len(num_str[i])):
        num_str[i][j] = int(num_str[i][j])
sum =[]
for i in xrange(len(num_str)):
    for j in xrange(len(num_str[i])-3):
        sum.append(num_str[i][j]*num_str[i][j+1]*num_str[i][j+2]*num_str[i][j+3])
for i in xrange(len(num_str)-3):
    for j in xrange(len(num_str[i])):
        sum.append(num_str[i][j]*num_str[i+1][j]*num_str[i+2][j]*num_str[i+3][j])
for i in xrange(len(num_str)-3):
    for j in xrange(3,len(num_str[i])):
        sum.append(num_str[i][j]*num_str[i+1][j-1]*num_str[i+2][j-2]*num_str[i+3][j-3])
for i in xrange(len(num_str)-3):
    for j in xrange(len(num_str[i])-3):
        sum.append(num_str[i][j]*num_str[i+1][j+1]*num_str[i+2][j+2]*num_str[i+3][j-3])
print max(sum)
