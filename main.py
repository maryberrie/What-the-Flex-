import jinja2
import webapp2
import logging
import os
import json
import datetime
import urllib
import urllib2
from google.appengine.api import users
from google.appengine.ext import ndb

env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

class information(ndb.Model):
    Name = ndb.StringProperty()
    Street = ndb.StringProperty()
    City = ndb.StringProperty()
    State = ndb.StringProperty()
    Phonenumber = ndb.StringProperty()

class Page(webapp2.RequestHandler):
    def get(self):

        template = env.get_template('page.html')

        self.response.out.write(template.render())

class store_property(webapp2.RequestHandler):
    def post(self):
        information_key = ndb.Key('information')



app = webapp2.WSGIApplication([
        ('/', Page),
], debug = True
)
