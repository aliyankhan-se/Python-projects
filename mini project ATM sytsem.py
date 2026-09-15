#basic ATM system

balance=20000
attempts=0
access=False #intial value is false for access
while(attempts<3):
    pin=int(input("ENTER YOUR 4 DIGIT PIN::"))
    print("════════════════════════════════")
    if(pin==2859):
        access=True  #then if the user enter coreect pin the value of access changes to True
        break
    attempts=attempts+1
    print("INCORRECT PIN,PLEASE ENTER CORRECT PIN.")
else:
    print("YOUR ACCOUNT BLOCKED DUE TO WRONG ATTEMPTS.")
    
if(access==True):#will check the current value of acees that will be true for entering to the next loop but if pin wrong then will be false and will not enter to the loop.
    while True:
         print("╔══════════════════════════════╗")
         print("║                              ║")
         print("║      WELCOME TO MY BANK      ║")
         print("║      ¯­­­¯¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­­­­¯­­­¯­­­¯­­­­­­¯­­­¯      ║")
         print("║      SECURE ATM SERVICE      ║")
         print("║      ¯­­­¯¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­­­­¯­­­¯­­­¯­­­­­­¯­­­¯      ║")
         print("╚══════════════════════════════╝")
         print("╔══════════════════════════════╗")
         print("║          ATM MENU            ║")
         print("╠══════════════════════════════╣")
         print("║  1. Check Balance            ║")
         print("║  ­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­­­­¯­­­¯­­            ║")
         print("║  2. Withdraw Cash            ║")
         print("║  ­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­­­­¯­            ║")
         print("║  3. Deposit Cash             ║")
         print("║  ­­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯            ║")
         print("║  4. Exit                     ║")
         print("║  ¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­¯­­­­­­¯­­­¯­­­¯­­­­­­¯­­­¯            ║")
         print("╚══════════════════════════════╝")
         choice=int(input("ENTER A CHOICE:"))
         print("--------------")
         if(choice==1):
            print("your Current balance is:",balance) 
            print("-----------------------------")
            cont=input("DO YOU WANT TO CONTINUE TRANSACTION(Y/N):")
            if(cont.lower()=="no"):
                break

         elif(choice==2):
            withdraw=int(input("ENTER AMOUNT TO WITHDRAW:"))
            print("-----------------------------")
            if(withdraw<=balance):
                balance=balance-withdraw
                print("MONEY WITHDRAWN SUCCESSFULLY:",withdraw)
                print("----------------------------------")
                print("NEW BALANCE:",balance)
                print("------------------")
                cont=input("DO YOU WANT TO CONTINUE YOUR TRANSACTION(Y/N):")
                if(cont.lower()=="no"):
                    break
            else:
                print("INSUFFICENT AMOUNT")
                print("------------------")
    
         elif(choice==3):
            balance=balance+int(input("ENTER AMOUNT TO DEPOSITE:"))
            print("------------------------------")
            print("SUCCESSFULLY DEPOSITED")
            print("----------------------")
            print("NEW BALANCE:",balance)
            print("-----------------")
            cont=input("DO YOU WANT TO CONTINUE TRANSACTION(Y/N):")
            if(cont.lower()=="no"):
                break
         elif(choice==4):
            print("╔══════════════════════════════╗")
            print("║     THANKYOU FOR USING       ║")
            print("║            ATM               ║")
            print("╚══════════════════════════════╝")
            
            break
    
