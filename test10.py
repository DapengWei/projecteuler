import math
import time
starttime = time.clock()
def prime_detect(num):
	for x in xrange(2,int(math.ceil(math.sqrt(float(num))+1))):
		if num == 2:
			return True
		else:
			if num%x == 0:
				return False
	return True
i = 2
sum = 0
while i <= 2000000:
	if prime_detect(i):
		sum = sum + i
	i = i+1
elapsed = time.clock()-starttime
print sum,elapsed 
