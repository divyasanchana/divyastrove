x=input()
x=int(x)
s=[]
mul=0
for i in range(1,6):
	mul=x*i
	s.append(str(mul))
s=' '.join(s)
print(s)
