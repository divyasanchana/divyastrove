N=input()
N=int(N)
lst=input()
lst=lst.split(" ")
s=set(lst)
s=list(s)
sort=sorted(s)
M=len(sort)
answer=[]
for i in range(0,M):
	count=0
	for j in range(0,N):
		if sort[i]==lst[j]:
			count=count+1
	if count>1:
		answer.append(sort[i])
if len(answer)==0:
	print("unique")
else:
	print(" ".join(answer))
