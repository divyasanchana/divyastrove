x=int(raw_input())

if(x%4==0):
	
	if(x%100==0):
		
		if(x%400==0):
			
			print("Hurray! It's a leap year")
		
		else:
			
			print("Nope. It's not a leap year")
	
	else:
	   
		print("Hurray! It's a leap year")	


else:
	
	
	print("Nope. It's not a leap year")

