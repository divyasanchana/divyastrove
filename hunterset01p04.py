n=input()
n=int(n)
string=input()
lst=string.split(" ")
ans=[]
for i in range(0,n):
	temp=lst[i]
	count=0
	for j in range(0,n):
		if temp==lst[j]:
			count=count+1
	if count==1:
		ans.append(lst[i])
print(''.join(ans))
