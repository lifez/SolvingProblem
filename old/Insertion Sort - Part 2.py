def insertionSort(ar):    
    for i in range(1,len(ar)):
        key = ar[i]
        j = i
        while j>0 and ar[j-1]>key:
            ar[j]=ar[j-1]
            j-=1
        ar[j] = key
        print " ".join(map(str,ar))
