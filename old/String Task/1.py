ans = ""
x = raw_input()
x = x.lower()
vovel = "aeiouy"
for i in x:
	if i in vovel:
		ans+=""
	else:
		ans+= "."+i
print ans