def chk_hit(dod,d,dragon):
	hit=0
	while d!=0:
		if d%dod ==0 and dragon[d-1]==1 :
			hit+=1
			dragon[d-1]=0
		d-=1
	return hit
k, l, m, n, d = [int(raw_input()) for _ in range(5)]	
"""
k = int(raw_input())
l = int(raw_input())
m = int(raw_input())
n = int(raw_input())
d = int(raw_input())
"""
dragon = []
x =0
hit = 0
while x<d:
	dragon.append(1)
	x+=1
hit+=chk_hit(k,d,dragon)
hit+=chk_hit(l,d,dragon)
hit+=chk_hit(m,d,dragon)
hit+=chk_hit(n,d,dragon)
print hit