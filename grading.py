from statistics import mean as m
import sqlite3 as db
import json

connection = db.connect('grading.db')
connection.row_factory = db.Row
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS student(first text, last text, grades text)")
allRecords = cursor.execute("SELECT * FROM student").fetchall()

def addGrades():
  gradeList = []

  firstName = input('Student first name: ')
  lastName = input('Student last name: ')
  gradeString = 'Assign grade to ' + firstName + ' ' +  lastName + ': '
  grade = input(gradeString)

  # Query string and database query executed
  query = "SELECT * FROM student WHERE first='" + firstName.lower() + "' AND last='" + lastName.lower() + "'"
  results = cursor.execute(query).fetchall()

  if results:
    for record in results:
      gradeList = json.loads(record["grades"])
      gradeList.append(float(grade))
      gradeList = json.dumps(gradeList)

      updateString = "UPDATE student SET grades = '" + gradeList + "' WHERE first='" + firstName.lower() + "' AND last='" + lastName.lower() + "'"
      cursor.execute(updateString)
  else:
    gradeList.append(float(grade))
    gradeList = json.dumps(gradeList)
    insertString = "INSERT INTO student VALUES('" + firstName.lower() + "','" + lastName.lower() + "','" + gradeList + "')"
    cursor.execute(insertString)

  prompt('\n\nGrade added. Please select another action:')



def removeStudent():
  firstName = input('Student first name: ')
  lastName = input('Student last name: ')

  query = "SELECT * FROM student WHERE first='" + firstName.lower() + "' AND last='" + lastName.lower() + "'"
  results = cursor.execute(query).fetchall()

  if results:
    for record in results:
      deleteString = "DELETE FROM student WHERE first='" + firstName.lower() + "' AND last='" + lastName.lower() + "'"
      cursor.execute(deleteString)
      prompt('\n\nStudent removed. Please select another action:')
  else:
    prompt('\n\nThat student does not exist! Please select another action:')



def studentAverage():
  firstName = input('Student first name: ')
  lastName = input('Student last name: ')

  query = "SELECT * FROM student WHERE first='" + firstName.lower() + "' AND last='" + lastName.lower() + "'"
  results = cursor.execute(query).fetchall()

  if results:
    for record in results:
      grades = json.loads(record["grades"])
      print('Student average grade:',m(grades))
      prompt('\n\nPlease select another action:')
  else:
    prompt('\n\nThat student does not exist! Please select another action:')
    


def classAverage():
  query = "SELECT * FROM student"
  results = cursor.execute(query).fetchall()
  averageList = []

  if results:
    for record in results:
      grades = json.loads(record["grades"])
      averageList += grades
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
  if (name == 'Admin') and (password == '123456'):
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
      connection.commit()
      connection.close()
      print('Thanks for using the Prefered Youth Training Helper Online Network. Bye!')
    else:
      invalidAction()


# Trigger login
# login()
prompt()