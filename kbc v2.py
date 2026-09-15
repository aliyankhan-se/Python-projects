score=0
prize=0

questions=[
    ["1).What is the largest country in the world?","A).Russia","B).China","C).India","D).America","A"],
    ["2).Who is the current President of USA?","A).Barrack Obama","B).Bill Clinton","C).Donald-J-Trump","D).Elon Musk","C"],
    ["3).Which planet is called Red Planet","A.Earth","B).Venus","C).Mars","D).Jupitar","C"],
    ["4).What is the largest ocean in the world?","A).Atlantic ocean","B).Pacific ocean","C).Artic ocean","D).India Ocean","B"],
    ["5).How many days are ther in leaf year","A).365","B).366","C).367","D).368","B"]
]
while True:
    print("╔═══════════════════════════════════════════════╗")
    print("║                  WELCOME TO                   ║")
    print("║            KAUN BANEGA CROR PATHI             ║")
    print("╚═══════════════════════════════════════════════╝")
    for question in questions:
        for i in question[0:5]:
            print(i)
        attempt=0
        while True:
            answer=input("CHOOSE CORRECT OPTION:")
            print("===================================")
            if(answer.upper()==question[5]):
                print("-YOUR ANSWER IS CORRECT!")
                print("-----------------------------------")
                score=score+1
                prize=prize+100000
                print("-YOUR SCORE IS:",score)
                print("-CONGRATULATION YOU WON:",prize,"PKR")
                print("-----------------------------------\n")
                break

            attempt=attempt+1
            if(attempt==1):
                print("-WRONG ANSWER!")
                print("-YOU HAVE ANOTHER CHANCE TO TRY!")
            
            else:
                print("-SORRY AGAIN WRONG ANSWER,MOVING TO NEXT QUESTION")
                print("-YOUR SCORE IS:",score)
                print("-----------------------------------------------\n")
                break
    print("========== GAME RESULT==========")
    print("-YOUR TOTAL SCORE IS:",score)
    print("-YOUR PRIZE MONEY:",prize,"PKR")
    print("-CONGRATULATION YOU WON THE GAME!") 
    print("---------------------------------\n")   

    again=input("-DO YOU WANT TO PLAY THE GAME AGAIN?")
    if(again.upper()=="no"):
        print("-THANKYOU FOR PLAYING GAME!")
        break
     

