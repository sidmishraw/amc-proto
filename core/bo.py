# bo.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-21 00:40:06
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-23 16:39:59


'''
The core module contains the business objects.
'''

class Address(object):
  'The address class'

  def __init__(self, street_address, city, state, country, postal_code):
    '''
    Needs street address, city, state, country and postal code as inputs\
    All of them are strings.
    '''
    
    self.street_address = street_address
    self.city = city
    self.state = state
    self.country = country
    self.postal_code = postal_code



class Person(object):
  '''
  The person - always plays the actor role in this relationship.
  '''

  def __init__(self, first_name, middle_name, last_name, address):
    'Initializes the Person object.'
    
    self.first_name = first_name
    self.middle_name = middle_name
    self.last_name = last_name
    self.address = address



class Employee(object):
  '''
  The employee - a role played by the person.
  '''

  def __init__(self, empId, actor, emailId, password):
    '''
    Initializes the Employee object for the given employeeID, actor and emailId.
    '''
    
    self.empId = empId
    self.actor = actor
    self.emailId = emailId
    self.password = password


class ManagementPolicy:
  'The management policy contains the hierarchy of reporting between employees'

  def __init__(self, manager, reportees=[]):
    '''
    Needs the manager and the list of reportees.
    '''
    
    self.manager = manager
    self.reportees = reportees




class Task(object):
  'The task object'


  def __init__(self, taskId, task_name, description, setup_date, \
    completion_date, task_setter, assigned_to, is_complete = False):
    '''
    Initializes a task that is assigned to an employee by their manager.
    '''

    self.taskId = taskId
    self.task_name = task_name
    self.description = description
    self.setup_date = setup_date
    self.completion_date = completion_date
    self.is_complete = is_complete
    self.task_setter = task_setter
    self.assigned_to = assigned_to



