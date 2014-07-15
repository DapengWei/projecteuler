# -*- coding: utf-8 -*-
import math
def Pentagonal(x):
	return x*(3*x-1)/2

def check_Pentagonal(y):
	z = (math.sqrt(24.0*y + 1.0) + 1.0 ) / 6
	if z == int(z):
		return True
	else:
		return False
k = 1
flag = True
while (flag):
	k = k + 1
	p_k = Pentagonal(k)
	for j in xrange(k-1,0,-1):
		p_j = Pentagonal(j)
		p_D = p_k - p_j
		p_S = p_k + p_j
		if check_Pentagonal(p_D) and check_Pentagonal(p_S):
			print "success",p_D
			flag = False