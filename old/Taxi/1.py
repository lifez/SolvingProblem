limit = int(raw_input())
x = raw_input("").split(" ")
x.sort(reverse=True)
x = [int(i)for i in x ]
j = limit-1
ans = 0
i = 0
while i<=j:
	ans+=1
	four = 4-x[i]
	while x[j]<=four and j>=i:
		four-=x[j]
		j-=1
	i+=1
print ans