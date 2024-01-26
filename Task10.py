a=input().split()
n=int(input())
ln=len(a)
i=0
cnt=1
while int(i)<ln:
 if int(a[i])>=n:
  cnt+=1
 i+=1
print(cnt)