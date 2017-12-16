x=int(raw_input())

rem1=x%400

rem2=x%4

if(rem1==0 and rem2==0):
	
	print("Hurray! It's a leap year")

else:
	
	print("Nope. It's not a leap year")
