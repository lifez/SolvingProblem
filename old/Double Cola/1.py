Name =  ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

x = int(raw_input())
y = 5
while True:
	if x<=y:
		y/=5
		print Name[(x-1)/y]
		break
	else:
		x-=y
		y*=2
