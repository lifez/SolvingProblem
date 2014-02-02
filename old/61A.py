x = raw_input()
y = raw_input()
ans = []
for (i,j) in zip(x,y):
	if (i=="1" and j=="1") or (i=="0" and j=="0"):
		ans.append(0)
	else:
		ans.append(1)
print ''.join(str(i) for i in ans)
