from google.appengine.ext import ndb
from google.appengine.ext.db import stats

tkey = ndb.Key('user','newUser')


class user(ndb.Model):
    userid = ndb.IntegerProperty()
    name = ndb.StringProperty(required=True)
    email= ndb.StringProperty(required=True)
    password=ndb.StringProperty()
    userActive = ndb.BooleanProperty()

    
def addUser(info):
    newUser = user(parent=ndb.Key('user','newUser'))
    newUser.userid = info["userid"]
    newUser.name = info["name"]
    newUser.email = info["email"]
    newUser.password = info["password"]
    newUser.put()
    return "Success"
    
    
    

def isEmpty():
    global_stat = stats.GlobalStat.all().get()
    return global_stat is None



def fetchUsers():
    r = user.query().order()
    res = r.fetch()
    if len(res) < 1:
        return False 
    else:
        return res
    
def checkUserPresence(_name):
    qry = user.query(user.name == _name)
    res = qry.fetch(1)
    if len(res) < 1:
        return False
    else:
        return True 
    
def checkLogin(_name,_pass):
    qry = user.query()
    qry.filter(user.name == _name)
    res = qry.fetch(1)

    
    if str(res[0].password) == str(_pass):
        return True
    else:
        return False 
    
    