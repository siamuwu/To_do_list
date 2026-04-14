print ("---------TO DO LIST---------\n")
menu = ['Add Task', 'View Task', 'Mark as Completed', 'Delete Task', 'Exit']
def display_menu(menu):
    for i, item in enumerate (menu, start=1):
        print(i,'. ', item)

tasks = []
def add_task(tasks):
    tasks.append(input('Enter Task: '))
    return tasks

def view_task(tasks):
    if tasks:
        for i, it in enumerate (tasks, start=1):
            print(i, '. ', it,'\n-------------------------------------')
    else:
        print('No tasks entered')

def mark_completed(tasks):
    try:
        cmpl = int(input('Enter the Task no. you completed: '))
    except ValueError:
        print('Please enter a number')
    if 1 <= cmpl <= len(tasks):
        tasks[cmpl - 1] = tasks[cmpl - 1] + "✅"
        print("Marked task as completed.")
    else:
        print("Task not found !")
        return

def delete_task(tasks):
    try:
        dl = int (input('Enter the Task no. you want to delete: '))
    except ValueError:
        print('Please enter a number')
    if 1 <= dl <= len(tasks):
        tasks.pop(dl - 1)
        print ("Deleted Task.")
    else:
        print ("Task not found !")
        return



while True:
    display_menu(menu)
    try:
        choice_user = int(input('Enter choice: '))
    except ValueError:
        print('Please enter a number')

    if choice_user == 1:
        add_task(tasks)
        print ('Task Added')

    elif choice_user == 2:
        view_task(tasks)

    elif choice_user == 3:
        mark_completed(tasks)

    elif choice_user == 4:
        delete_task(tasks)

    elif choice_user == 5:
        break

    else:
        print ('Invalid Choice')
