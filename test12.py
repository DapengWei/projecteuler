import math
import time
starttime = time.clock()
#create prime
prime_list=[2]
def prime_create(ordinal):
	num = prime_list[-1]+1
	while (len(prime_list)-1) <= ordinal:
		flag = True
		for x in xrange(2,int(math.ceil(math.sqrt(float(num))+1))):
			if num%x == 0:
				flag = False
				break
		if flag:
			prime_list.append(num)
		num = num+1
	return prime_list[ordinal]

#create triangle
def triangle_number(num_x):
	num_y=(num_x+1)*num_x/2
	return num_y

triangle_number_ordinal = 7

while 1:
	num_triangle = triangle_number(triangle_number_ordinal)
	prime_num = 0
	prime_num_list=[]
	prime_num_dict={}
	num_triangle_remainder = num_triangle
	while prime_create(prime_num) <= num_triangle_remainder:
		i = 0
		k = num_triangle
		while k%prime_create(prime_num) == 0:
			i = i+1
			k = k/prime_create(prime_num)
		if i !=0:
			prime_num_list.append(i)
			prime_num_dict[prime_create(prime_num)]=i
		num_triangle_remainder = num_triangle
		if len(prime_num_dict) == 0:
			pass
		else:
			for l in prime_num_dict:
				num_triangle_remainder = num_triangle_remainder / (l*prime_num_dict[l])
		#print prime_num,prime_create(prime_num),prime_num_dict,num_triangle_remainder
		prime_num = prime_num+1
	divisor_ordinal = 1
	for j in xrange(len(prime_num_list)):
		divisor_ordinal = divisor_ordinal*(prime_num_list[j]+1)
	elapsed = time.clock()-starttime
	#print prime_num_list
	#print triangle_number_ordinal,num_triangle,divisor_ordinal,prime_num_dict,elapsed
	if divisor_ordinal > 500:
		print triangle_number_ordinal,num_triangle,divisor_ordinal,elapsed
		break
	triangle_number_ordinal = triangle_number_ordinal + 1