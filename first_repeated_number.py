N=input()
N=int(N)
lst=input()
lst=lst.split(" ")
ans=[]
for i in range(0,N):
	count=0
	for j in range(0,N):
		if lst[i]==lst[j]:
			count=count+1
	if count>1:
		ans.append(lst[i])
if len(ans)==0:
	print("unique")
else:
	print(ans[0])
