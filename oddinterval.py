x=input()
y=input()
x=int(x)
y=int(y)
for i in range(x,y,2):
	if (i%2)==0:
		print (i+1)
	else:
		print (i)
