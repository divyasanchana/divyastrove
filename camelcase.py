str=input()
str1=str.split(" ")
c=[]
for i in str1:
	f=i[0].upper()+i[1:]
	c.append(f)
str2 = ' '.join(c)
print(str2)
