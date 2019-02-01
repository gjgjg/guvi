number=int(input())
array=list(map(int,input().split()))
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]<array[j]:
            array[i],array[j]=array[j],array[i]
for i in array:
    print(i,end='')
