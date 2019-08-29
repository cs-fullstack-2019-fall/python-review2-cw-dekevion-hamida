
taskList=["sweep the floor","clean the bathroom","do the laundry","cut the grass"]

def listAlltasksfunc():
    for i in taskList:
        f = open("file.txt","w")
        f.write(i)

        print(i)
def addToList(newtask):
    taskList.append(newtask)
def deleteTask(taskTodelete):
    taskList.remove(taskTodelete)


menu = -1
while menu != 4:
    menu = int(input('What would you like to do next \n'
                     '1. List all tasks \n'
                     '2. Add a task to the list \n'
                     '3. Delete a task. \n'
                     '4. To quit the program : '))
    if menu == 1:
        print('The task List is:')
        listAlltasksfunc()

    if menu == 2:
        taskNew= input('Add to the task list here:   ')
        f = open("file.txt","w")
        f.write(taskNew)
        f.close()
        addToList(taskNew)
    if menu == 3:
        removeTask= input('what task would you like to delete ?  ')
        deleteTask(removeTask)

