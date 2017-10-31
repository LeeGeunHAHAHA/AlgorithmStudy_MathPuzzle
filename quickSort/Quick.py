def quickSort(a, head, tail) :
    print(head,tail)
    if (head == tail) : return 
    print(tail)
    pivot = a[tail]
    h =head
    t = tail-1
    while (h<t) :
        while a[h] <= pivot : h+=1
        while a[t] > pivot : t-=1
        if h <= t: a[h] , a[t] = a[t] , a[h]
        print(a)
    a[t+1] , a[tail]= a[tail], a[t+1]
    print("!!!!!!!!!!!!!!!!!!!")
    print(a)
    print("!!!!!!!!!!!!!!!!!!!")
    return quickSort(a,head,t)
    return quickSort(a,h,tail)
    return

a = [ 7, 8, 5, 2, 4, 9, 6]

quickSort(a,0,len(a)-1)
print(a)
