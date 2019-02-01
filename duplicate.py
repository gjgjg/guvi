number=int(input())
array=list(map(int,input().split()))
duplicate_list=[]
for i in array:
    if array.count(i)>1 and i not in duplicate_list:
        duplicate_list.append(i)
print(*sorted(duplicate_list))
