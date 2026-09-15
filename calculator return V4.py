# lets make calculator using functions
while True:
    print("=======CALCULATOR======")
    print("1) Addition(+)")
    print("2) Subtraction(-)")
    print("3) Multiplication(*)")
    print("4) Division(/)")
    print("5) Floor Division(//)")
    print("6) Modulas(%)")
    print("7) Exponenent(**)")
    print("8) Exit")
    print("=======================")
    # choice=int(input("Enter operation:"))
    # num1=int(input("Enter 1st number:"))
    # num2=int(input("Enter 2nd number:"))
#first creating functions
    def addition(a,b):
        return a+b
        # print("Addition of",a,"+",b,":",a+b)

    def subtraction(a,b):
        return a-b
        # print("subtraction of",a,"-",b,":",a-b)

    def multiplication(a,b):
        return a*b
        # print("Multiplication of",a,"*",b,":",a*b)

    def division(a,b):
        if(b==0):
            print("CANNOT DIVIDED BY ZERO")
        else:
            return a/b
            # print("Division  of",a,"*",b,":",a/b)

    def floor_division(a,b):
        if(a<0 or b<0):
            print("NEGATIVE NUMBER IS NOT ALLOWED")
        else:
            return a//b
            # print("Floor Division of",a,"*",b,":",a//b)

    def modulas(a,b):
        return a%b
        # print("Modulas of",a,"*",b,":",a%b)

    def exponent(a,b):
        return a**b
        # print("Exponenet of",a,"*",b,":",a**b)

#now calling function
    choice=int(input("Enter operation:"))
    if(choice==8):
        print("THANKS FOR USING CALCULATOR")
        break
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))

    if(choice==1):
        add=addition(num1,num2)
        print("Addition of",num1,"+",num2,":",add)
    elif(choice==2):
        sub=subtraction(num1,num2)
        print("Subtraction of",num1,"-",num2,":",sub)
    elif(choice==3):
        mul=multiplication(num1,num2)
        print("Multiplication of",num1,"*",num2,":", mul)
    elif(choice==4):
        div=division(num1,num2)
        print("Division of",num1,"/",num2,":",div)
    elif(choice==5):
        f_div=floor_division(num1,num2)
        print("Floor Division of",num1,"//",num2,":",f_div)
    elif(choice==6):
        mod=modulas(num1,num2)
        print("Modulas of",num1,"%",num2,":",mod)
    elif(choice==7):
        expo=exponent(num1,num2)
        print("Exponenet of",num1,"**",num2,":",expo)
    else:
        ("INVALID CHOICE")
    
