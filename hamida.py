## Create a new task List
taskList=["sweep the floor","clean the bathroom","do the laundry","cut the grass"]
##########################################################
# Function to print the new list to console and to the text file

def listAlltasksfunc():
    f = open("file.txt","a")
    f.write('\nThis is the new list\n')
    for i in taskList:
        f.write(i)
        f.write('\n')
        print(i)
#######################################################
# Function to ask user for new task and add to the list
def addToList(newtask):
    taskList.append(newtask)
#######################################################
# Function to ask user to remove task from the list

def deleteTask(taskTodelete):
    taskList.remove(taskTodelete)

#####################################################
# Menu
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
        # f = open("file.txt","a")
        # f.write('\nThe New Task is : ')
        # f.write(taskNew)
        # f.write('\n')
        # f.close()
        addToList(taskNew)
    if menu == 3:
        removeTask= input('what task would you like to delete ?  ')
        deleteTask(removeTask)

