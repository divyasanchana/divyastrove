x=input()
y=input()
x=int(x)
y=int(y)
s=[]
for i in range(x+1,y):
	n=i
	flag=0
	for j in range(2,n-1):
		if(i%j==0):
			flag=1
	if flag!=1:		
		s.append(str(i))
c=' '.join(s)
print(c)
