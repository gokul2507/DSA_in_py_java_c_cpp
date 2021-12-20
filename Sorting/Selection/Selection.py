n=int(input())
l=list(map(int,input().split()))
for i in range(n):
     min_index=i
     for j in range(i+1,n):
          if l[min_index]>l[j]:
               min_index=j
     if min_index!=i:
          l[min_index],l[i]=l[i],l[min_index]
print(*l)