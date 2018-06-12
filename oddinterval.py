x=input()
y=input()
x=int(x)
y=int(y)
c=[]
for i in range(x,y,2):
	if (i%2)==0:
		c.append (str(i+1))
	else:
		c.append (str(i))
print(c)
c=' '.join(c)
print(c)
