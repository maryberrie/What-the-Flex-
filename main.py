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

class Page(webapp2.RequestHandler):
    def get(self):

        template = env.get_template('page.html')

        self.response.out.write(template.render())

class store_property(webapp2.RequestHandler):
    def post(self):
        information_key = ndb.Key('information',)
        information = information_key.get()
        if not information:
            information = Information(name = self.request.get('name'),
                                      street = self.request.get('street'),
                                      city = self.request.get('city'),
                                      state = self.request.get('state'),
                                      zipcode = long(self.request.get('zipcode')),
                                      phonenumber = long(self.request.get('number1')),
                                                    long(self.request.get('number2')),
                                                    long(self.request.get('number3')))
            information.key = information_key
            information.put()
        template = env.get_template('data.html')
<<<<<<< HEAD
        self.response.out.write(template.render())
=======
<<<<<<< HEAD
        variables = {
            "information": information,
        }
        self.response.out.write(template.render(variables))

class Page(webapp2.RequestHandler):
    def get(self):
        query = Information.query().order(-Information.name)
        information = query.fetch()

        template = env.get_template('page.html')
        variables = {
            "information": information,
        }
        self.response.out.write(template.render(variables))
=======
        self.response.out.write.(template.render())
>>>>>>> be0504258e84489e4b833c0426c2b0bd2beaab62

>>>>>>> 68ae4ce208dfd8ee9b20b1f0469f45bdd134a113


app = webapp2.WSGIApplication([
        ('/', Page),
        ('/store_property', store_property)
], debug = True
)
