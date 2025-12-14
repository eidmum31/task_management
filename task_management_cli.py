users={} #empty dictionary for storing the users

def signUp():
    userName=input("Enter your user name: ")
    password=input("Enter your password: ")
    if(len(userName)>0 and len(password)>0): #checking for empty fields
        if userName in users:
            print("Users Already Exists\n\n")   
            return
        else:
            users[userName]= {"tasks":[], "password":password} #creating new users
            print("New user created\n\n")
    else:
        print("Please enter both name and password\n\n")

def signIn():
    userName=input("Enter your user name: ")
    password=input("Enter your password: ")
    if(userName in users and users[userName]['password']==password):
        print("Signed In successfully\n\n") #validating user id
        return userName
    else:
        print("Invalid user name or password\n\n")
             
def addNewTask(loggedUser):
    newTask=input("Enter new task : ")
    users[loggedUser]['tasks'].append(
        {
            'name':newTask,
            'status':False
        }
    )

def viewTasks(loggedUser):
    tasks=users[loggedUser]['tasks']
    
    if len(tasks)==0:
        print("No task is assinged\n\n")
        
    else:
        for i,task in enumerate(tasks):
            print("Task {}: {}".format(i+1,task['name']))
            print("Task Complete? : {}\n\n".format(task['status'])) 

def completeTask(loggedUser):
    viewTasks(loggedUser)
    if len(users[loggedUser]['tasks'])==0:
        return
    taskNumber= int(input("Enter task number to complete : "))
    if(taskNumber>len(users[loggedUser]['tasks'])):
        print("Invalid task number\n\n")
    else:
        users[loggedUser]['tasks'][taskNumber-1]['status']=True
        print("Task is completed\n\n")

def deleteTask(loggedUser):
    viewTasks(loggedUser)
    if len(users[loggedUser]['tasks'])==0:
        return
    taskNumber= int(input("Enter task number to delete : "))
    if(taskNumber>len(users[loggedUser]['tasks'])):
        print("Invalid task number\n\n")
        
    else:
        users[loggedUser]['tasks'].pop(taskNumber-1)
        print("Task is deleted\n\n")

def crud(loggedUser):
    while(True):
        print("1. View Tasks\n2. Add Tasks\n3. Complete Tasks\n4. Delete Task\n5. Log Out\n\n")
        choice= input("Please enter your choice : ")
        if choice=='1':
            viewTasks(loggedUser)
        elif choice=='2':
            addNewTask(loggedUser)
        elif choice=='3':
            completeTask(loggedUser)
        elif choice=='4':
            deleteTask(loggedUser)
        elif choice=='5':
            break
        else:
            print("Invalid Choice")
        
def application():
    while(True):
        print("1. Sing Up\n2. Log In\n3. Exit\n\n")
        choice= input("Please enter your choice : ")
        if choice == '1':
            signUp()
        elif choice=='2':
            user=signIn()
            if user:
                crud(user)
        elif choice=='3':
            break
        else:
            print("Invalid Choice")
application()