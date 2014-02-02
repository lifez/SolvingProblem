n = int(raw_input())
HeightSoilder = map(int,raw_input().split())
MaxIndex = HeightSoilder.index(max(HeightSoilder))
temp =0
count=0
while MaxIndex>0:
	count+=1
	temp = HeightSoilder[MaxIndex-1]
	HeightSoilder[MaxIndex-1]=HeightSoilder[MaxIndex]
	HeightSoilder[MaxIndex]= temp
	MaxIndex-=1
MinHeight = min(HeightSoilder)
MinIndexList = [i for i,j in enumerate(HeightSoilder) if j==MinHeight]
MinIndex = MinIndexList[len(MinIndexList)-1]
for i in range(MinIndex,n-1):
	count+=1
	temp = HeightSoilder[i-1]
	HeightSoilder[i-1] = HeightSoilder[i]
	HeightSoilder[i] = temp
print count

