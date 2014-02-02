x = int(raw_input())
cap = 0
maxcap =0
for i in range(x):
	passen = map(int,raw_input().split())
	cap-=passen[0]
	cap+=passen[1]
	if cap>maxcap:
		maxcap = cap
print maxcap