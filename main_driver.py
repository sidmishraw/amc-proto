# main_driver.py
# -*- coding: utf-8 -*-
# @Author: sidmishraw
# @Date:   2017-01-21 00:22:26
# @Last Modified by:   sidmishraw
# @Last Modified time: 2017-01-21 00:28:49


from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def root():
  'The root of the server, just return the index.html'
  return render_template('index.html')



if __name__ == '__main__':
  app.run()