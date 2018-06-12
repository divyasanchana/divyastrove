x=input()
n=len(x)
x=int(x)
original=x
sum=0
rem=0
for i in range(1,n+1):
	rem=int(x%(10))
	x=int(x/(10))
	sum=sum+(rem**n)
if sum==original:

	print("yes")
else:
	print("no")
