def insertionSort(ar):
    count =0
    for i in range(1,len(ar)):
        key = ar[i]
        j = i
        while j>0 and ar[j-1]>key:
            count+=1
            ar[j]=ar[j-1]
            j-=1
        ar[j] = key
    print count    
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
 
