print("Xin Chao! This program captures the marks for one or more students, and prints results. ")
loop=0
while loop==0:
	name=str(input("Enter the student's name: "))
	marks=[0,0,0,0,0,0]
	result=["Passed","Passed","Passed","Passed","Passed","Passed"]
	subjects=["Maths","Science","Social","English","Hindi","Kannada"]
	totalmarks=0
	for x in range(len(subjects)):
		print("Enter your",subjects[x]," marks (Out of 100) : ")
		marks[x]=int(input(""))
		while marks[x]>100 or marks[x]<0:
			print("TRY'NA PLAY GAMES WITH ME, EH? YOU FAILED THO")
			print("Enter again! (because the marks should be between 0 - 100)")
			marks[x]=int(input(""))
		if marks[x]<35:
			result[x]=("Failed")
		totalmarks=(totalmarks+marks[x])
	percentmarks=(totalmarks/len(subjects))
	print("*****  start of  R E S U L T S  *****")
	for x in range(len(subjects)):
		if result[x]=="Passed":
			print("In",subjects[x],name," got",marks[x],"Hence, the student","\033[5;30;42m",result[x]," \033[0m")
		else:
			print("In",subjects[x],name," got",marks[x],"Hence, the student","\033[15;36;41m",result[x]," \033[0m")
	if percentmarks>=75:
		grade=("Distinction")
	elif percentmarks>=60 and percentmarks<75:
		grade=("1st class")
	elif percentmarks>=50 and percentmarks<60:
		grade=("2nd class")
	elif percentmarks>=35 and percentmarks<50:
		grade=("3rd class")
	else:
		grade=("failed")
	if grade=="failed":
		statement=("you kidding me?",name," seriously failed, LOL. Study Harder!")
	else: 
		statement=("Well done!")
	print("Total Marks =",totalmarks,"/600"" Percentage Marks = ",round(percentmarks,2),"%"" Grade = ", grade," ",statement)
	print("*****  end of  R E S U L T S  *****")
	loop=int(input("Do you want to enter another student's details? Type (0)- Yes ; (1)- No : "))
print("End of program, thank you!")








