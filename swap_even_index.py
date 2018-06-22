string=input()
n=len(string)
string=list(string)
temp=0
if n%2==0:
	for i in range(0,n-1,2):
		temp=string[i]
		string[i]=string[i+1]
		string[i+1]=temp
string=''.join(string)
print(string)
