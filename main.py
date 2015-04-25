"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask,request, session, g, redirect, url_for, abort, render_template, flash,jsonify
    
from google.appengine.api import urlfetch
from google.appengine.api import taskqueue
from google.appengine.ext import deferred
import logging
from model import *
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'




@app.route('/',methods=['GET'])
def index():
     return render_template('index.html')

  







@app.route('/addUser',methods=["POST"])
def addNewUser():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    
    info = {"userid":1,
            "name":username,
            "email":email,
            "password":password
            }
    return jsonify(status=addUser(info))
           
@app.route('/getUsers',methods=['GET'])
def getUsers():
    logging.info(fetchUsers())
    return str(fetchUsers())

@app.route('/login',methods=['POST'])
def login():
    if 'loggedin' in session:
        return jsonify({"status":True})

    name = str(request.form["username"])
    password = str(request.form["password"])
    status=checkLogin(name,password)

    if status==True:
        session["loggedin"]=True
    return jsonify(status=status)



@app.route('/checkUser',methods=['POST'])
def checkUser():
    _name = str(request.form["name"])
    return jsonify(present=checkUserPresence(_name))
    





@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500








def expensive():
    url = "http://requestb.in/14a2ouj1"
    result = urlfetch.fetch(url)
    logging.info(result.status_code)
    
#deferred.defer(expensive)


@app.route('/deferred')
def deferred():
    
    return "Deferred."




@app.route('/queue')
def queue():
    taskqueue.add(url='/fetch')
    return "Queued."
    




@app.route('/fetch',methods=["GET","POST"])
def fetch():
    url = "http://requestb.in/14a2ouj1"
    result = urlfetch.fetch(url)
    if result.status_code == 200:
        return "Done."
        

