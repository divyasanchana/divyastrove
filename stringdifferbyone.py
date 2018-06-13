string1=input()
string2=input()
n1=len(string1)
n2=len(string2)
lst1=list(string1)
lst2=list(string2)
count=0
if n1==n2:
	n=n1=n2
	for i in range(0,n):
		if lst1[i]!=lst2[i]:
			count=count+1
if count==1:
	print("yes")
