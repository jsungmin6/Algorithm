def solution2(a):
  a=a.replace('S','ASA')
  a=a.replace("D","ADA")
  a=a.replace("T",'ATA')
  a=a.replace("#","#A")
  a=a.replace("*","*A")
  a=a.split('A')
  print(a)

  for i, j in enumerate(a):
    if j=='S':
      a[i]=int(a[i-1])**1
      a[i-1]=0
    elif j=="D":
      a[i]=int(a[i-1])**2
      a[i-1]=0
    elif j=='T':
      a[i]=int(a[i-1])**3
      a[i-1]=0
    elif j=='#':
      a[i]=int(a[i-1])*(-1)
      a[i-1]=0
    elif j=='*':
      a[i]=int(a[i-1])*2
      a[i-1]=0
      for k in range(i-1,0,-1):
        if a[k]!=0:
          a[k]=2*a[k]
          break

    elif j=="":
      a[i]=int(0)
  res=0
  print(a)
  for i in a:
    res+=i
  return res

print(solution2('0D*'))
