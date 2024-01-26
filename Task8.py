a=input().split()
maxx=99999
for i in a:
 if int(i)>0 and int(i)<int(maxx):
  maxx=i
print(maxx)