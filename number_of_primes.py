x=input()
y=input()
x=int(x)
y=int(y)
count=0
for i in range(x,y+1):
	n=i
	flag=0
	for j in range(2,n-1):
		if(i%j==0):
			flag=1
	if flag!=1:		
		count=count+1
print(count)
