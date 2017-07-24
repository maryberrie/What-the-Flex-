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

class Information(ndb.Model):
    name = ndb.StringProperty()
    street = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    phonenumber = ndb.StringProperty()

class Page(webapp2.RequestHandler):
    def get(self):

        template = env.get_template('page.html')

        self.response.out.write(template.render())

class store_property(webapp2.RequestHandler):
    def post(self):
        information_key = ndb.Key('information')
        information = information_key.get()
        if not information:
            information = Information(name = self.request.get('name'), street = self.request.get('street'),
                                      city = self.request.get(), state = self.request.get('state'),
                                      phonenumber = self.request.get('number1'),self.request.get('number2'), self.request.get('number3'))
            information.key = information_key
            information.put()
        template = env.get_template('data.html')
        self.response.out.write.(template.render())



app = webapp2.WSGIApplication([
        ('/', Page),
], debug = True
)
