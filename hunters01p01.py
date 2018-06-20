N=input()
N=int(N)
lst=input()
lst=lst.split(" ")
s=set(lst)
s=list(s)
sor=sorted(s)
M=len(sor)
ans=[]
for i in range(0,M):
	count=0
	for j in range(0,N):
		if sor[i]==lst[j]:
			count=count+1
	if count>1:
		ans.append(sor[i])
if len(ans)==0:
	print("unique")
else:
	print(" ".join(ans))
