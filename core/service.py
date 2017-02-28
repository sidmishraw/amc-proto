# service.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-02-23 11:09:34
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-27 21:33:05


# app specific imports
from core.bo import Task
from core.bo import Employee


# python standard library imports
from json import dumps
from json import loads
from json import JSONDecoder
from json import JSONEncoder
from datetime import datetime


# for generating random unique ids for the tasks
from uuid import uuid4


# service.py
# will be used to store the data.
# I will move this to a DB once I'm sure of the schema.
user_dict = {'admin':'admin', 'manager':'pass123', 'employee':'employee'}
global_dict= {}
tasks_dict = {}




def check_login_credentials(username, password):
  '''
  Checks the user credentials for login

  :return: True or False
  '''

  global user_dict, employees

  if username not in employees or employees[username].password != password:

    return False
  else:
    return True




def create_task(task_name, recipient_email_address, task_description,\
  setter_email_address):
  '''
  Creates a task and adds it to the tasks_dict

  :param: task_name str  - Name of the task
  :param: recipient_email_address str - Email address of the person
   the task is being assigned to.
  :param: task_description str - task description

  :return: None
  '''

  global tasks_dict

  task = Task(taskId = str(uuid4()), \
      task_name = task_name, \
      description = task_description, \
      assigned_to = recipient_email_address, \
      task_setter = setter_email_address, \
      setup_date = datetime.now())

  tasks_dict[task.taskId] = task

  print(tasks_dict)

  return




def get_all_created_tasks(task_owner):
  '''
  Fetches all the tasks create by the person.

  :param: task_owner str - Is the emailId of the task owner (creator)

  :return: list(str(Task)) - where list is the list of json strings for Task obj
  '''

  global tasks_dict

  created_tasks = []

  sorted_tasks = sorted(tasks_dict.values(), key = lambda task: task.setup_date, reverse = True)

  for task in sorted_tasks:
    if task.task_setter == task_owner:
      created_tasks.append(str(task))

  return created_tasks





def get_all_tasks_assigned(task_owner):
  '''
  Fetches all the tasks assigned to the person.

  :param: task_owner str - Is the emailId of the task owner

  :return: list(str(Task)) - where list is the list of json strings for Task obj
  '''

  global tasks_dict

  my_tasks = []

  sorted_tasks = sorted(tasks_dict.values(), key = lambda task: task.setup_date, reverse = True)

  for task in sorted_tasks:
    if task.assigned_to == task_owner:
      my_tasks.append(str(task))

  return my_tasks




def mark_task_complete(taskId):
  '''
  Marks the task as complete.

  :param: taskId str - The unique taskId

  :return: None
  '''

  global tasks_dict

  tasks_dict[taskId].is_complete = True
  tasks_dict[taskId].completion_date = datetime.now()

  print(tasks_dict)

  return str(tasks_dict[taskId])


