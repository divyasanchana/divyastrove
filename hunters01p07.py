N=input()
N=int(N)
lst=input()
lst=lst.split(" ")
ans=[]
if N%2==0:
	for i in range(0,N,2):
		if int(lst[i])%2!=0:
			ans.append(lst[i])
		
		if int(lst[i+1])%2==0:
			ans.append(lst[i+1])
		
	print(' '.join(ans))
else:
	if int(lst[0])%2!=0:
		ans.append(lst[0])
	for i in range(1,N,2):
		if int(lst[i])%2==0:
			ans.append(lst[i])
			
		if int(lst[i+1])%2!=0:
			ans.append(lst[i+1])
	print(' '.join(ans))
	
