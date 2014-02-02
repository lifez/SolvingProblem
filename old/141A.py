x,y,z= [raw_input() for _ in range(3)]
newword = x+y
count =0
for i in newword:
	if newword.count(i)==z.count(i):
		count+=1
print "YES" if count==len(z) and len(newword)==len(z) else "NO"