x=input()
y=input()
x=int(x)
y=int(y)
s=[]
for i in range(x+1,y):
	n=len(str(i))
	original=int(i)
	sum=0
	rem=0
	for j in range(1,n+1):
		rem=int(i%(10))
		i=int(i/(10))
		sum=sum+(rem**n)
	if sum==original:
		s.append(str(original))
c=' '.join(s)
print(c)
