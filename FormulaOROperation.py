print("Bonjour! This program can be used for calculating the area and perimeter; and can also be used for finding the formulae of the shapes :) ")
fororop=int(input(" Type- (1)-Area and Perimeter; (2)-Formulae : "))
if fororop==1:
	print("You have chosen for computing area and perimeter!")
	operation=int(input("Do you want to compute the Area or Perimeter? Type: (1)-Area ; (2)-Perimeter : "))
	if operation==1:
		shape=int(input("Which shape's area do you want to compute? Type: (1)-Square ; (2)-Rectangle ; (3)-Circle ; (4)-Trapezium :"))
		if shape==1:
			print("You have chosen Square!")
			side=int(input("Enter the side of the square:"))
			areaofsq=(side**2)
			print(areaofsq)
		elif shape==2:
			print("You have chosen Rectangle!")
			length=int(input("Please enter the length of the rectangle:"))
			breadth=int(input("Please enter the breadth of the rectangle:"))
			areaofrect=(length*breadth)
			print(areaofrect)
		elif shape==3:
			print("You have chosen Circle!")
			radius=int(input("Please enter the radius of the circle:"))
			areaofcirc=(3.14*radius**2)
			print(areaofcirc)
		elif shape==4:
			print("You have chosen Trapezium!")
			p1=int(input("Please enter the first parallel line:"))
			p2=int(input("Please enter the second parallel line:"))
			height=int(input("Please enter the height of the trapezium:"))
			areaoftrap=((p1+p2)/2*height)
			print(areaoftrap)
		else:
			print("**error**")
	elif operation==2:
		shape=int(input("Which shape's perimeter do you want to compute? Type: (1)-Square ; (2)-Rectangle ; (3)-Circle ; (4)-Trapezium :"))
		if shape==1:
			print("You have chosen Square!")
			side=int(input("Enter the side of the square:"))
			periofsq=(side*4)
			print(periofsq)
		elif shape==2:
			print("You have chosen Rectangle!")
			length=int(input("Please enter the length of the rectangle:"))
			breadth=int(input("Please enter the breadth of the rectangle:"))
			periofrect=(2*length+2*breadth)
			print(periofrect)
		elif shape==3:
			print("You have chosen Circle!")
			radius=int(input("Please enter the radius of the circle:"))
			periofcirc=(2*3.14*radius)
			print(periofcirc)
		elif shape==4:
			print("You have chosen Trapezium!")
			l1=int(input("Please enter the measurement of the first line :"))
			l2=int(input("Please enter the measurement of the second line :"))
			l3=int(input("Please enter the measurement of the third line :"))
			l4=int(input("Please enter the measurement of the fourth line :"))
			perioftrap=(l1+l2+l3+l4)
			print(perioftrap)
	else:
		print("**error**")
elif fororop==2:
	print("You have chosen to find Formulae!")
	shape=int(input("Type: (1)-Square; (2)-Rectangle; (3)-Triangle; (4)-Circle; (5)-Trapezium : "))
	if shape==1:
		print("You have chosen square!")
		oper=int(input("Do you want the formula for The (1)-area or (2)-perimeter? "))
		if oper==1:
			print("Area= side x side")
		elif oper==2:
			print("Perimeter= 4 x side")
		else:
			print("try'na be smart, eh? you failed tho")
	elif shape==2:
		print("You have chosen rectangle!")
		oper=int(input("Do you want the formula for The area or perimeter? "))
		if oper==1:
			print("Area= length x breadth")
		elif oper==2:
			print("Perimeter= 2(length+breadth)")
		else:
			print("try'na be smart, eh? you failed tho")
	elif shape==3:
		print("You have chosen triangle!")
		oper=int(input("Do you want the formula for The area or perimeter? "))
		if oper==1:
			print("Area= 1/2(base x height)")
		elif oper==2:
			print("Perimeter= side A + side B + side C")
		else:
			print("try'na be smart, eh? you failed tho")
	elif shape==4:
		print("You have chosen circle!")
		oper=int(input("Do you want the formula for The area or perimeter? "))
		if oper==1:
			print("Area= 3.141592653589793238462643 x radius^2")
		elif oper==2:
			print("Perimeter= 2 x 3.141592653589793238462643 x radius  or 3.141592653589793238462643 x diameter")
		else:
			print("try'na be smart, eh? you failed tho")
	elif shape==5:
		print("You have chosen trapezium!")
		oper=int(input("Do you want the formula for The area or perimeter? "))
		if oper==1:
			print("Area= 1/2(parallel 1 + parallel 2)height")
		elif oper==2:
			print("Perimeter= side 1 + side 2 + side 3 + side 4")
		else:
			print("try'na be smart, eh? you failed tho")
	else:
		print("try'na get smart, eh? wrong.")
else:
	print("bruh")





