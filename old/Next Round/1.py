limit,Smax = map(int, raw_input().split())
scores = map(int, raw_input().split())
ssum = 0
for score in scores:
	if score >0 and score>=scores[Smax-1]:
		ssum +=1


print ssum
		




