x=input()
y=input()
x=int(x)
y=int(y)
if y%2==0:
	y=y-1
c=[]
for i in range(x+1,y,2):
	if (i%2)!=0:
		c.append (str(i+1))
	else:
		c.append (str(i))
c=' '.join(c)
print(c)
