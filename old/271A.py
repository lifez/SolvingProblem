x = int(raw_input())
while True:
	x+=1
	a = 0
	y = str(x)
	for i in y:
		if y.count(i)>1:
			a=1
			break
	if a==0:
		print x 
		break