# main_driver.py
# -*- coding: utf-8 -*-
# @Author: sidmishraw
# @Date:   2017-01-21 00:22:26
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-03 23:26:21


from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import abort
from core import service

import os



app = Flask(__name__)



@app.route('/')
def root():
  'The root of the server, just return the index.html'
  return render_template('index.html')




@app.route('/login.html', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  elif request.method == 'POST':
    status = service.check_login_credentials(request.form['username_input'], \
                            request.form['password_input'])
    if status:
      return render_template('user_landing.html')
    else:
      return render_template('login.html')


if __name__ == '__main__':
  app.run()