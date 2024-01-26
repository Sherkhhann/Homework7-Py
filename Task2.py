def TwoLists():
 list_one=input().split()
 list_two=input().split()
 for i in list_one:
  if i in list_two:
   cnt+=1
  else:
   cnt=0
 if cnt>0:
  print("True")
 else:
  print("False")

TwoLists()