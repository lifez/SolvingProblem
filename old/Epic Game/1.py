from fractions import gcd
x,y,z = map(int, raw_input().split())
point = 0
while z>0:
	if point==0:
		z-=gcd(x,z)
		if z<=0:
			print 0
		else:
			point+=1
		
	elif point==1:
		z-=gcd(y,z)
		if z<=0:
			print 1
		else:
			point-=1