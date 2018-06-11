x=input()
n=int(x)
x=int(x)
flag=0
for i in range(2,n-1):
	if(x%i==0):
		flag=1
if flag==1:		
	print("no")
else:
	print("yes")
