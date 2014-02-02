x = int(input())
score = [int(x) for x in input().split()]
max = 0
min = 0
ans = 0
count = 0
for i in score:
	if count ==0:
		max = i 
		min = i
		count+=1
	elif i > max:
		max = i
		ans+=1
	elif i < min:
		min = i
		ans+=1
print (ans)