number=int(input())
array=list(map(int,input().split()))
print(*[i for i in array if array.count(i)==1])
            
