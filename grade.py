# this code ask a student his grade in 5 subjects then print the average grade

print("This program ask a student his grade in 5 subjects:")
history= int(input("what is your grade in History?\n\n"))
Maths= float(input("what is your grade in Maths?\n\n"))
sociology= int(input("what is your grade in sociologyy?\n\n"))
English= float(input("what is your grade in English?\n\n"))
chemistry= int(input("what is your grade in chemistry?\n\n"))
average_grade= int(history + Maths + sociology+English+chemistry)
print(average_grade/5)

if average_grade/5 > 90 or average_grade/5 > 80:
    print("you have an A grade")
    print ("you have a B")
elif average_grade/5 > 70 or average_grade/5 >60:
    print("you have a C")
    print("you have a D")
else:
    print("Failed")













