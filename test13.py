textfile = open("test13.txt","r")
num_list = textfile.readlines()
sum = 0
for i in xrange(len(num_list)):
    num_list[i] = num_list[i].strip("\n")
    num_list[i] = int(num_list[i])
    sum = sum + num_list[i] 
print sum