n=input()
n=int(n)
string=input()
lst=string.split(" ")
sort=sorted(lst)
rev=reversed(sort)
ans=list(rev)
print(''.join(ans))
