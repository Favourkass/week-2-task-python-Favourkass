from auth import authenticate
from contextlib import contextmanager
from datetime import datetime

logged_date = datetime.now()
'''
i used context manager to create and update my text files

i took info from the authenticate file as made available from the beginning.

used nested if else statement to check for conditions as described in the task.

imported datetime and created a variable for it in order to separate the date from the time 
to achieve the desired result of text to be updated to either access_denied.txt or 
access_granted.txt


'''

@contextmanager
def open_file(file, mode):
  access = open(file, mode)
  yield access

def resource_deco(email='example@email.com', password='passoword123'):
  
  def main_deco(function):
    user= authenticate(email, password)
    def wrapper():
      if user:
        if user['role'] == 'admin' or user['role'] == 'superadmin':
           print("Welcome" + " " + user['role'] + " " + user['first_name'])
           with open('access_granted.txt','a') as access:
             access.write(f'\n {user["role"]} {user["first_name"]} {user["last_name"]} viewed company resources on {logged_date.strftime("%x")} at {logged_date.strftime("%I")}:{logged_date.strftime("%M")}')
           return function()
        else:
          with open('access_denied.txt','a') as access:
             access.write(f'\n {user["role"]} {user["first_name"]} {user["last_name"]} tried to view company most valuable resources on {logged_date.strftime("%x")} at {logged_date.strftime("%I")}:{logged_date.strftime("%M")}')
          print("Welcome " + user['first_name'] )
          
          return 'You are not allowed to view resources'
          
          
      else:
        print("Only staff can access this resource")
    return wrapper
  return main_deco
  
  
  