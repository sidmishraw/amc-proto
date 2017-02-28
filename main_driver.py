# main_driver.py
# -*- coding: utf-8 -*-
# @Author: sidmishraw
# @Date:   2017-01-21 00:22:26
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-27 23:06:03


# flask related imports
from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import url_for
from flask import abort
# for jsonifying the result
# since flask only allows strings and templates
# to be returned from the view
from flask import jsonify

# app specific imports
from core import service

# python standard library imports
from os import environ
from json import dumps





# the flask application
app = Flask(__name__)



# APP ROUTE MAPS

@app.route('/')
def root():
  'The root of the server, just return the index.html'
  return render_template('index.html')

@app.route('/manager')
def root_manager():
  'The root of the server for the dummy manager account, just return the index.html'
  return render_template('index.html', is_manager = True)


@app.route('/employee')
def root_employee():
  'The root of the server for the dummy employee account, just return the index.html'
  return render_template('index.html', is_manager = False)


# @app.route('/login.html', methods=['GET', 'POST'])
# def login():
#   if request.method == 'GET':
#     return render_template('login.html')
#   elif request.method == 'POST':
#     status = service.check_login_credentials(request.form['username_input'], \
#                             request.form['password_input'])
#     if status:
#       return render_template('user_landing.html')
#     else:
#       return render_template('login.html')





# BINDING TASK RELATED SERVICE METHODS



@app.route('/create_task', methods=['POST'])
def create_task():
  '''
  Creates the task from the form.

  :return: None
  '''

  task_name = request.form['task_name']
  recipient_email_address = request.form['recipient_email_address']
  task_description = request.form['task_description']
  setter_email_address = request.form['setter_email_address']

  service.create_task(task_name = task_name,\
    recipient_email_address = recipient_email_address,\
    task_description = task_description,\
    setter_email_address = 'manager@amc.com')

  return 'True'




@app.route('/get_all_tasks_assigned', methods=['POST'])
def get_all_tasks_assigned():
  '''
  Fetches all the tasks assigned to the user.

  :return: str - The JSON string for all the tasks assigned to the user
  '''

  task_owner = request.form['task_owner']

  tasks = service.get_all_tasks_assigned(task_owner)

  return dumps(tasks)





@app.route('/get_all_created_tasks', methods=['POST'])
def get_all_created_tasks():
  '''
  Fetches all the tasks created by the user.

  :return: str - The JSON string for all the tasks created by the user.
  '''

  task_owner = request.form['task_owner']

  tasks = service.get_all_created_tasks(task_owner)

  return dumps(tasks)




@app.route('/mark_task_complete', methods=['POST'])
def mark_task_complete():
  '''
  Marks the task as complete.

  :return: None
  '''

  task_id = request.form['task_id']

  print('task_id = {}'.format(task_id))

  updated_task = service.mark_task_complete(task_id)

  # return the updated_task as is since it is already
  # a JSON string, check my __repr__ for Task class.
  return updated_task




if __name__ == '__main__':

  # Bind to PORT if defined, otherwise default to 5000.
  port = int(environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
  # debug mode on for local development
  # app.run(debug=True)

