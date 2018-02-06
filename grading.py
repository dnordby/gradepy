from ast import literal_eval
from os import path
from statistics import mean as m

def addGrades():
  name = input('Student name: ')
  gradeString = 'Assign grade to ' + name + ': '
  grade = input(gradeString)
  if name in grades.keys():
    print('Adding grade...')
    grades[name].append(float(grade))
  else: 
    print('Student doesn\'t exist. Creating...')
    gradeList = []
    gradeList.append(float(grade))
    grades[name] = gradeList

  print(grades)
  prompt('\n\nGrade added. Please select another action:')



def removeStudent():
  name = input('Name of student to remove: ')

  if name in grades.keys():
    del grades[name]
    prompt('\n\nStudent removed. Please select another action:')
  else:
    prompt('\n\nThat student does not exist! Please select another action:')



def studentAverage():
  name = input('Name of student to average scores: ')

  if name in grades.keys():
    print('Student average grade:',m(grades[name]))
    prompt('\n\nPlease select another action:')
  else:
    prompt('\n\nThat student does not exist! Please select another action:')
    


def classAverage():
  averageList = []
  if len(grades) > 0:
    for k,v in grades.items():
      for grade in v:
        averageList.append(grade)

    print('Class average grade:',m(averageList))
    prompt('\n\nPlease select another action:')
  else:
    prompt('You have no students in the class!')



def invalidAction():
  prompt('\n\nThat is not a valid option. Please choose from the list below (enter number):')



def validate(action):
  try:
    return isinstance(int(action) ,int)
  except ValueError as v:
    prompt('\n\nPlease enter the NUMBER of the action you would like to perform:')
  except Exception as e:
    prompt('\n\nThat is not a valid option. Please choose from the list below:')



def login():
  name = input('Enter username: ')
  password = input('Enter password: ')
  if (name == 'Admin') and (password == 'dn9922'):
    prompt()
  else:
    print('Login failure. Please try again.')
    login()



def prompt(prompt="\n\nHello, what would you like to do today?"):
  output = '''
  [1] Enter grades for a student
  [2] Remove a student from the course
  [3] Get a single student's average grade
  [4] Get the class average grade
  [5] Exit
  '''
  print(prompt)
  print(output)

  action = input('>> ')

  if validate(action):
    action = int(action)
    if action == 1:
      addGrades()
    elif action == 2:
      removeStudent()
    elif action == 3:
      studentAverage()
    elif action == 4:
      classAverage()
    elif action == 5:
      # Save file on exit
      gradeString = str(grades)
      writableGradefile = open('grades.txt','w')
      writableGradefile.write(gradeString)
      writableGradefile.close()
      print('Thanks for using the Perfect Youth Training Helper Online Network. Bye!')
    else:
      invalidAction()



# INITIATE PROGRAM
if path.isfile('./grades.txt'):
  readableGradefile = open('grades.txt','r')
  filedata = readableGradefile.read()
  grades = literal_eval(filedata)
  readableGradefile.close()
else:
  grades = {}

# Trigger login
login()