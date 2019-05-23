n=int(input())
arr=set(map(int,input().split()))
s=0
for x in range(len(arr)-1,0,-1):
    s+=x
print(s)
