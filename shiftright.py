def main():
	get=input()
	get=get.split(" ")
	N=get[0]
	K=get[1]
	N=int(N)
	K=int(K)
	l=input()
	l=l.split(" ")
	print(l)
	for i in range(0,K):
		shift(l,N)
	print(l)
def shift(l,N):
	temp=l[N-1]
	for i in range(N-1,0,-1):
		l[i]=l[i-1]
	l[0]=temp
	return(l)
main()
