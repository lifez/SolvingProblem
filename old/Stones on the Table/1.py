def all_equal(array):
	return all(x==array[0] for x in array)

x = int(raw_input())
instone = raw_input()
n = len(instone)
count = 0
i=0
while i<x-1:
	if instone[i]==instone[i+1]:
		count+=1
	i+=1
if all_equal(instone):
	count = x-1
print count