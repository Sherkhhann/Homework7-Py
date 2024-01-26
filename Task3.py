def SecondSmallest():
 numbers=input().split()
 smallest=99999
 for i in numbers:
  if int(i)<=int(smallest):
   smallest=i
 print(smallest)

SecondSmallest()