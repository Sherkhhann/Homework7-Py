a=input().split()
maxx=-99999
index_maxx=0
i=0
length_a=len(a)
while i<length_a:
 if int(a[i])>int(maxx):
  maxx=a[i]
  index_maxx=i
 i+=1
print(maxx, end=" ")
print(index_maxx)
