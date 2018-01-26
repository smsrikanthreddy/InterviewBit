A = [ 0, 0, -1, 0 ]
sub1 = []
sub2 = []
suba = []
counta = 1
for num in A:
 if num >= 0:
  counta += 1
  suba.append(num)
for num in range(counta):
  if counta%2 == 0:
    half = int(counta/2)
    sub1 = suba[0:half]
    sub2 = suba[half:]
  else:
    cnt = counta+1
    half = int(cnt/2)
    sub1 = suba[0:half]
    sub2 = suba[half:]
sum1 = 0
sum2 = 0
for sa in sub1:
 sum1 += sa
for sb in sub2:
 sum2 += sb
if(sum1 > sum2):
  return sub1
else:
  return sub2
if (sum1 == sum2 and len(sum1) > len(sum2)):
 return sub1
else:
 return sub2
if (sum1 == sum2 and len(sum1)== len(sum2) and sub1[0] > sub2[0]):
 return sub1
else:
 return sub2