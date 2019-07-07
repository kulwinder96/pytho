s=input('enter string')
count=0
count1=0
count2=0
count3=0
for c in s:
 if c in 'a' or c in 'i' or c in 'e' or c in 'o' or c in 'u':
  count=count+1
 elif c in '1' or c in '2' or c in '3' or c in '4' or c in '5' or c in '6' or c in '7' or c in '8' or c in '9' or c in '0':
  count2=count2+1
 elif c in 'b' or c in 'c' or c in 'd' or c in 'f' or c in 'g' or c in 'h' or c in 'j' or c in 'k' or c in 'l' or c in 'm' or c in 'n' or c in 'p' or c in 'q' or c in 'r' or c in 's' or c in 't' or c in 'v' or c in 'w' or c in 'x' or c in 'y' or c in 'z':
  count1=count1+1
 else:
  count3=count3+1
print('Vowels is ',count)
print('consonants',count1)
print('numbers ',count2)
print('others',count3)