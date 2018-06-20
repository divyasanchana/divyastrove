n=input()
n=int(n)
string=input()
lst=string.split(" ")
ans=[]
for i in range(0,n):
	if int(lst[i])==i:
		ans.append(str(i))
if len(ans)==0:
	print("-1")
else:
	print(' '.join(ans))
