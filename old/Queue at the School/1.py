n,t = map(int,raw_input().split())
children = raw_input()
children=list(children)
while t>0:
	i=0
	while i<n-1:
		if children[i]=="B" and children[i+1]=="G":
			children[i]="G"
			children[i+1]="B"
			i+=2
		else:
			i+=1
	t-=1
print "".join(children)
