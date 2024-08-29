data = []

def input_task():
    e_task = input("enter you task : ")
    data.append(e_task)

def viwe_task():
    print(data)

def delete_task():
    try:
        task_number = int(input("Enter the task number to delete: "))
        if task_number in data:
            del data[task_number]
            print(f"Task {task_number} deleted.")
        else:
            print("Invalid task number. Task not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

print("---chooce option---")
print("1. input you task's : ")
print("2. viwe task : ")
print("3. enter number to delete task")

while True:
    choices = ('1','2','3','4')
    chooce = ("chooce one option : ")
    if chooce in choices:
        if chooce == '1':
            input_task()

        if chooce == '2':
            viwe_task()

        if chooce == '3':
            delete_task()

        if chooce == '4':
            break
    else:
        print("enter corect option \n\t\t plz try again !")
