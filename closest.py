#functionclosest_power
def closest_power(x, y):
 i=1
 count=1
 j=1
 count1=0
 val=0
#loop for finding power
 while True:
  i=i*x
  if i>=y:break
  count=count+1
 if i==y:
  val=i
 else:
#second loop for find lesthen power
  while count1<count-1:
   j=j*x
   count1=count1+1
 range1=i-y
 range2=y-j
#conditions for print values 
 if range1>range2:
  val=j
  count=count1
 elif range1==range2:
  val=j
  count=count1
 else:
  val=i

 return count , val

while True:
 try:
  base=input('enter base number')
  if base.startswith('-'):
   print('invalid input please enter positive number')
   continue
  base=int(base)
  break
 except:
  print('invalid input')
  continue
while True:
 try:
  num=input('enter number')
  if num.startswith('-'):
   print('invalid input enter positivenumber')
   continue
  num=int(num)
  break
 except:
  print('invalid input')
  continue
print(closest_power(base, num))
