li=list(map(int,input().split()))
k=int(input())
pairs=[]
c=0
for num in li:
    pairs.append(k-num)
    if num in pairs:
        fp=num
        c=1
        break
if c==1:
    print(True)
    print(str(k-num)+"+"+str(num))
elif c==0:
    print(False)
