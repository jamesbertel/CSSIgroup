from google.appengine.ext import ndb

class User(ndb.Model):
    username =  ndb.StringProperty(required=True)
