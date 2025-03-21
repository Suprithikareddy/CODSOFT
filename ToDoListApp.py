#### Welcome to the todolist app


tasks=[]

def addtask():
        task = input("Please enter a task:")
        tasks.append(task)
        print(f" Task '{task}' added to the list.")


def listtasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Currently available tasks:")
        for index, task in enumerate(tasks):
            print(f"Task {index}.{task}")


def deletetask():
    listtasks()
    try:
        tasktodelete = int(input("Enter the task that you want to delete:"))
        if tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"Task {tasktodelete} has been deleted.")
        else:
            print("Task to be removed has not found.")
    except:
        print("Invalid input entered.")
    
if __name__=="__main__":

   
    print("Welcome to the To Do List App in Python")
    while(True):
        print("\n")
        print("Please select any one of the following options:")
        print("...................")
        print("1. Add a task")
        print("2 . Delete a task")
        print("3. List all the tasks")
        print("4. Quit")

        choice = int(input("Enter a choice:"))
        if(choice == 1):
            addtask()
        elif (choice ==2):
            deletetask()
        elif (choice ==3):
            listtasks()
        elif( choice ==4):
            break
        else:
            print("Enter a valid input.")

    print("Good luck next time!")

       