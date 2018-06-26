n=input()
n=int(n)
lst=[]
ans=[]
for i in range (0,n):
	str=input()
	lst.append(str)
length=len(lst[0])
for i in lst:
	for j in lst:
		for k in range(0,length):
			if i[k]==j[k]:
				ans.append(i[k])
for i in ans				
print(ans)
	
