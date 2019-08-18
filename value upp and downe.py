class volume:
 x=1
 def upper(y):
  y.x +=1
  return y.x
 def down(z):
  z.x -=1
  return z.x
vol=volume()
a=1
while True:
 num=input('enter upp for volume upp and type down for low volume')
 if num=='upp' or num=='UPP':
  print(vol.upper())
 elif num =='down' or num=='DOWN':
  print(vol.down())
 else:
  print(num,' is invalid key word')