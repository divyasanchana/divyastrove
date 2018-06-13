string=input()
temp=string.split(" ")
x=temp[0]
y=temp[1]
n1=len(x)
n2=len(y)
temp=list(temp)
if n1==n2:
	n=n1
	for i in range(0,n):
		if temp[0][i]!=temp[1][i]:
			temp[0]=temp[0].replace(temp[0][i],temp[1][i])
w1=temp[0]
w2=temp[1]
if w1==w2:
	print("yes")
else:
	print("no")
