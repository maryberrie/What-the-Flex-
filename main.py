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
    def get(self):

        query = Information.query().order(-Information.name)
        information = query.fetch()
        template = env.get_template('data.html')
        variables = {
            "information": information
        }
        self.response.out.write(template.render(variables))


    def post(self):
<<<<<<< HEAD
        information_key = ndb.Key('Information',self.request.get('name') )
=======
        information_key = ndb.Key('Information', self.request.get('name'))
>>>>>>> 8b7c91b0d7f48adf526572f97189c1389784f529
        information = information_key.get()
        if not information:
            information = Information(name = self.request.get('name'),
                                      street = self.request.get('street'),
                                      city = self.request.get('city'),
                                      state = self.request.get('state'),
                                      zipcode = long(self.request.get('zipcode')),
                                      phonenumber = long(self.request.get('number')))
<<<<<<< HEAD
            information_key = information.key
            information.put()
        template = env.get_template('data.html')
=======
            information.key = information_key
            information.put()
>>>>>>> 8b7c91b0d7f48adf526572f97189c1389784f529
        variables = {
            "information": information
        }
        template = env.get_template('data.html')

        self.redirect('/store_property')

class Page(webapp2.RequestHandler):
    def get(self):


        template = env.get_template('page.html')
<<<<<<< HEAD
        variables = {
            "information": information,
        }
        self.response.out.write(template.render(variables))
=======

        self.response.out.write(template.render())


>>>>>>> 8b7c91b0d7f48adf526572f97189c1389784f529


app = webapp2.WSGIApplication([
        ('/', Page),
        ('/store_property', store_property)
], debug = True)
