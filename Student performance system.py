#PROJECT "STUDENT PERFORMANCE SYSTEM"


#FUNCTION 1
def total_marks(java,python,c_plus,c_sharp,html):
   return java+python+c_plus+c_sharp+html

#FUNCTION 2
def calculate_avg(total):
   return total/5
#FUNCTION 3
def calculate_grade(average):
   if(average>=90):
      return "A+"
   elif(average>=80):
      return "A"
   elif(average>=70):
      return "B"
   elif(average>=60):
      return "C"
   elif(average>=60):
      return "D"
#FUNCTION 4
def check_status(s1,s2,s3,s4,s5):
   if(s1<50 or s2<50 or s3<50 or s4<50 or s5<50):
      return "FAIL"
   else:
      return "PASS"
#FUNCTION 4
def performance_report(name,id,department,semester,java,python,c_plus,c_sharp,html,total,average,grade,status):
   print("=============================")
   print("     PERFORMANCE REPORT")
   print("=============================")
   print("NAME      :",name)
   print("ID        :",id)
   print("DEPARTMENT:",department)
   print("SEMESTER  :",semester)
   print("=============================")
   print("       SUBJECT MARKS")
   print("=============================")
   print("JAVA\t:",java)
   print("PYTHON\t:",python)
   print("C_PLUS\t:",c_plus)
   print("C_SHARP\t:",c_sharp)
   print("HTML\t:",html)
   print("-----------------------------")
   print("TOTAL MARKS:",total)
   print("AVERAGE\t:",average)
   print("GRADE\t:",grade)
   print("STATUS\t:",status)
   print("=============================")


#intilizing these variables take phir choices ke andr jo variable ho jo return values ko store krte hai wo value between choice pass hosake take multiple function use use karsake.
#or han istrha values upadate hoge in variables mai take use access kare dosre choice mai function ko value pass krne ke liya
name=""
id=""
department=""
semester=""

java=0
python=0
c_plus=0
c_sharp=0
html=0

total=0
average=0
grade=0
status=""


#Menue
while True:
   print("===================================")
   print("    STUDENT PERFORMANCE SYSTEM")
   print("===================================")
   print("1. Enter Student Information")
   print("­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­¯­­­­¯­­­¯­­­­­­­¯­­­­­­­¯­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­¯­­­­")
   print("2. Calculate Total Marks")
   print("­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­¯­­­­¯­­­¯­­­­­­­¯­­­­­­­¯­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­¯­­­­")
   print("3. Calculate Average")
   print("­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­¯­­­­¯­­­¯­­­­­­­¯­­­­­­­¯­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­¯­­­­")
   print("4. Calculate Grade")
   print("­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­¯­­­­¯­­­¯­­­­­­­¯­­­­­­­¯­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­¯­­­­")
   print("5. Check Pass / Fail")
   print("­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­¯­­­­¯­­­¯­­­­­­­¯­­­­­­­¯­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­¯­­­­")
   print("6. Show Performance Report")
   print("­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­¯­­­­¯­­­¯­­­­­­­¯­­­­­­­¯­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­¯­­­­")
   print("7. Exit")
   print("===================================\n")

   choice=int(input("Enter choice:"))
   print("­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­¯­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­­­­­­")
   if(choice==1):
      print("=============================")
      print("    STUDENT INFORMATION")
      print("=============================")
      name=input("Enter Student Name:")
      id=input("Enter Student ID:")
      department=input("Department:")
      semester=input("Semester:")
      print("=============================")
      print("       SUBJECT MARKS")
      print("=============================")
      java=int(input("Enter JAVA marks:"))
      python=int(input("Enter PYTHON marks:"))
      c_plus=int(input("Enter C++ marks:"))
      c_sharp=int(input("Enter C SHARP marks:"))
      html=int(input("Enter HTML marks:"))
   elif(choice==2):
      total=total_marks(java,python,c_plus,c_sharp,html)
      print("TOTAL MARKS:",total)
      print("­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­¯­­­­­­­¯­¯­­­¯­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­¯­­­­")
   elif(choice==3):
      average=calculate_avg(total)
      print("AVERAGE:",average)
      print("­¯­­­¯­­­¯­­­¯­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­­­­­­­­­­­­¯­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­¯­­­­")
   elif(choice==4):
      grade=calculate_grade(average)
      print("GRADE:",grade)
      print("­¯­­­¯­­­­­­¯­­¯­­­¯­­­¯­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­¯­­­­")
   elif(choice==5):
      status=check_status(java,python,c_plus,c_sharp,html)
      print("STATUS:",status) 
      print("­¯­­­¯­­­¯­­­¯­­¯­­­¯­­­¯­­¯­­­­­­­­­­­­­­­­­­­­­­­­­­¯­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­¯­­­­")
   elif(choice==6):
      performance_report(name,id,department,semester,java,python,c_plus,c_sharp,html,total,average,grade,status)
      break
   




