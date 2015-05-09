num_file = file("test67.txt","r")
num_line = num_file.readlines()

for i in xrange(len(num_line)):
    num_line[i] = num_line[i].strip("\n")
    num_line[i] = num_line[i].split(" ")
    for j in xrange(len(num_line[i])):
        num_line[i][j] = int(num_line[i][j])
for i in xrange(len(num_line)):
    if i == 0:
        pass
    else:
        for j in xrange(len(num_line[i])):
            if j == 0:
                num_line[i][j] = num_line[i-1][j] + num_line[i][j]
            else:
                if j == len(num_line[i])-1:
                    num_line[i][j] = num_line[i-1][j-1] + num_line[i][j]
                else:
                    num_line[i][j] = num_line[i][j] + max(num_line[i-1][j],num_line[i-1][j-1])
print max(num_line[len(num_line)-1])