
from core import bo

user_dict = {'admin':'admin', 'manager':'pass123', 'employee':'employee'}

def check_login_credentials(username, password):
  '''
  Checks the user credentials for login
  :return: True or False
  '''
  global user_dict
  if username not in user_dict or user_dict[username] != password:
    return False
  else:
    return True
