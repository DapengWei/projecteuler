num_file = file("test18.txt","r")
num_line = num_file.readlines()

for i in xrange(len(num_line)):
	num_line[i] = num_line[i].strip("\n")
	num_line[i] = num_line[i].split(" ")
	for j in xrange(len(num_line[i])):
		num_line[i][j] = int(num_line[i][j])
for i in xrange(len(num_line)):
	