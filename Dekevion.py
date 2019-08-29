# Create a task list. A user is presented with the text below.
#Congratulations! You're running [YOUR NAME]'s Task List program.

# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program

# Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.
# Make each option a different function in your program.
# Do <strong>NOT</strong> use Google. Do <strong>NOT</strong> use other students. Try to do this on your own.
 #Extra Credit. Save the user's list in a text file. When the program is run again,
# input that text file so their task list is not lost.

import pickle

taskList=["sweep the floor","clean the bathroom","do the laundry","cut the grass"]
filename = 'file.txt'
with open('file.txt') as f:
    content = f.readlines()

def listAlltasksfunc():
    for i in taskList:
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
                     '4. To quit the program'))
    if menu == 1:
        print('The task List is:')
        listAlltasksfunc()

    if menu == 2:

        taskNew= input('Add to the task list here:   ')
        f = open("file.txt","a",)
        f.write(taskNew)
        f.close()
        addToList(taskNew)

    if menu == 3:
        removeTask=input('what task would you like to delete ?  ')
        deleteTask(removeTask)

