def task():
    tasks = [] #Empty list
    print("------Welcome To the To Do App--------")

    total_tasks = int((input("Enter how many tasks you want to enter = ")))
    for i in range(1, total_tasks+1):
        task_name = input (f"Enter tasks {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n {tasks}")

    while True:
        operation = int(input("Enter 1 - Add\n 2 - Update\n 3 - Delete\n 4 - View\n 5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter tasks you want to add = ") 
            tasks.append(add)
            print(f"Task {add} has been successfully added........")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks :
                up = input("Enter the new task = ")
                ind = tasks.index(updated_val)
                tasks [ind] = up
                print(f"Updated task {up}")

        elif operation == 3 :
            To_delete = input("Enter the task which you want to delete = ")
            if To_delete in tasks :
                ind = tasks.index(To_delete)
                del tasks [ind]
                print(f"Task {To_delete} has been deleted.......")

        elif operation == 4 :
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print ("Closing the program......")
            break

        else:
            print("Not available")

task()

