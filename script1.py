#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:38:54 2020

@author: deep
"""


from flask import Flask  #from flask library we are importing the Flask class
from flask import render_template #importing html templates that python flask library has.


app = Flask(__name__) #We are storing the value that return from the Flask class to a variable.
#__name__ :- special variable in which we get the name of the python script i.e. "main" if we execute this script1 
# but if we import this script1 into another script then script name becomes "script1" and then debug = True statement won't run

@app.route('/') #Decorator-@, '/'- Home Page
def home():
    return render_template("home.html")
    #return "Hello This is my First Web Application!!!!!"



@app.route('/about/')
def about():
    return render_template("about.html")
    
    #return "I am inside the about page!!!!!!!!!!!"



if __name__ == "__main__":
    app.run(debug = True)
    