def add_task():
    print("=====ADD TASK=====")
    while True:
        task=input("-Enter Task:")
        if(task in tasks):
            print("-Task Already Exist! ")
        else:
            tasks.append(task)
            print("-Task Added Succesfully!")
            print("------------------------\n")
        again=input("-Do You Want To Add Another Task?:")
        if(again=="no"):
            break

    
def view_task():
    print("=====CURRENT TASKS=====")
    if(tasks==[]):
        print("-No Task Avalilable!")

    counter=0
    for i in tasks:
        counter=counter+1
        print(counter,".",i,) 
        print("------------------") 
    print("\n") 
            

def remove_task():
    print("=====REMOVE TASK=====")
    while True:
        counter=0
        for i in tasks:
            counter=counter+1
            print(counter,".",i,)
            print("-------------")
        remove=int(input("Enter Task no to remove:"))
        if(remove>=1):
            tasks.pop()
            print("-Task Removed Successfully!")
        again=input("-Do You Want To Remove Another Task?:")
        if(again=="no"):
            break
     



def search_task():
   counter=0
   search=input("Search Your Task:")
   for task in tasks:
       counter=counter+1
       if search in task:
        print(counter,".",task)
       else:
           print("Task Not Found")

    

def update_task():
    print("=====UPDATE TASK=====")
    counter=0
    for i in tasks:
        counter=counter+1
        print(counter,".",i,)

    update=int(input("Enter Task No To Update:"))
    add_task=input("Enter New Task:")
    tasks[update-1]=add_task
    print("Task Added Sucessfully!\n")




tasks=[]
i=0

while True:
    print("======TO-DO-LIST-APP======")
    print("1.Add Task")
    print("-------------")
    print("2.View Task")
    print("-------------")
    print("3.Remove Task")
    print("-------------")
    print("4.Search Task")
    print("-------------")
    print("5.Update Task")
    print("-------------")
    print("6.Exit")
    print("==========================\n")

    choice=int(input("Enter Choice:"))

    if(choice==1):
        add_task()
    elif(choice==2):
        view_task()
    elif(choice==3):
        remove_task()
    elif(choice==4):
        search_task()
    elif(choice==5):
        update_task()
    elif(choice==6):
        print("Thankyou For Using To-Do-List App!")
        print("GoodBy!")
        break
    else:
        print("Invalid Choice! Please Enter Number From 1-5.")
        break