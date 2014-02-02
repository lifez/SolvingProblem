def chk(word):
	n=0
	for i in word:
		if i==i.lower():
			n+=1
	return n

x = raw_input()
if x[0]==x[0].lower() and chk(x)>1:
	print x
elif x[0]==x[0].lower() and chk(x)<=1:
	print x[0].upper()+x[1:].lower()
elif x==x.upper():
	print x.lower()
else:
	print x

