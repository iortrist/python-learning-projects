import os

taskList = []
options = {1: 'Add a new task', 2: 'Remove a task', 3: 'Display all task(s)', 4: 'Exit'}
choice = 0
message = ''

def addTask():
  task = input('Enter new task: ')
  taskList.append(task)
  return taskList[-1]

def removeTask():
  task = input('Select task to remove: ')
  return taskList.pop(int(task)-1)

def displayTask():
  count = 0
  if len(taskList):
    print('Active task(s):\n')
  for task in taskList:
    count += 1
    print(f'[{count}] - {task}')
 
def clearConsole():
  if os.name == 'nt':
        os.system('cls')
  else:
      os.system('clear')

while True:
  clearConsole()
  for key,value in options.items():
    print(f'[{key}] - {value}')

  if message != '':
    print(f'\n{message}')

  print(f'\nTotal active task(s): {len(taskList)}\n')

  try:
    choice = int(input('Select an option: '))
  except:
     message = 'Invalid option selected. Option must be integer.'
     continue

  clearConsole()
  displayTask()


  match choice:
     case 1:
        print()
        task = addTask()        
        message = f'"{task}" has been added to the list.'
     case 2:
        print()
        try:
          task = removeTask()
          message = f'"{task}" has been removed from the list.'
        except:
          message = 'Invalid option selected. Try again.'
     case 3:
        # displayTask()
        input('\nPress Enter to go back main menu')
     case 4:
        break
     case _:
        message = 'Invalid option selected. Try again.'