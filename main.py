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
    zipcode = ndb.IntegerProperty()
    phonenumber = ndb.IntegerProperty()

class Begin(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('begin.html')
        self.response.out.write(template.render())

class Begin2(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('begin2.html')
        self.response.out.write(template.render())

class Creepy(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('1creepy.html')
        self.response.out.write(template.render())

class Sunshine(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('1sunshine.html')
        self.response.out.write(template.render())

class Tree(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('1tree.html')
        self.response.out.write(template.render())

class Companion(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('2companion.html')
        self.response.out.write(template.render())

class InformationPage(webapp2.RequestHandler):
    def get(self):
        if  self.request.get('Enter').lower() == 'butterfly':
            template = env.get_template('page.html')
            self.response.out.write(template.render())
        else:
            template = env.get_template('form.html')
            self.response.out.write(template.render())

class AddInfo(webapp2.RequestHandler):
    def post(self):
        information_key = ndb.Key('Information', self.request.get('name'))
        information = information_key.get()
        if not information:
            information = Information(name = self.request.get('name'),
                                      street = self.request.get('street'),
                                      city = self.request.get('city'),
                                      state = self.request.get('state'),
                                      zipcode = long(self.request.get('zipcode')),
                                      phonenumber = long(self.request.get('number'))
                                      )
        """else:
            information.name = self.request.get('name')
            information.street = self.request.get('street')
            information.city = self.request.get('city')
            information.state = self.request.get('state')
            information.zipcode = long(self.request.get('zipcode'))
            information.phonenumber = long(self.request.get('number'))"""

        information.key = information_key
        information.put()

        self.redirect('/poro')




app = webapp2.WSGIApplication([
        ('/', Begin),
        ('/begin2', Begin2),
        ('/dark', Creepy),
        ('/sunshine', Sunshine),
        ('/tree', Tree),
        ('/poro', InformationPage),
        ('/companion', Companion),
        ('/porosave', AddInfo)
], debug = True)
