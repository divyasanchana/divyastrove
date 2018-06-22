str1=input()
str2=input()
n1=len(str1)
n2=len(str2)
if(n1==n2):
	sstr1=sorted(str1)
	sstr2=sorted(str2)
	if(sstr1==sstr2):
			print("Given strings are anagrams")
	else:
			print("Given strings are not anagrams")
else:
	print("Given srings are not of equal length")
