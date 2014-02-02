def insertionSort(ar):    
    x = len(ar)
    y = x-1
    V = ar[y]
    while y>0:
        if ar[y-1]> V:
            ar[y]=ar[y-1]
            y-=1
            print " ".join(map(str,ar))
        elif ar[y-1]<V:
            ar[y]=V
            break
    if ar[0]>V:
        ar[0]=V
        print " ".join(map(str,ar))
    else:
        print " ".join(map(str,ar))
