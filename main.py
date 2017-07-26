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
    kids = ndb.StringProperty()
    job = ndb.StringProperty()
    family = ndb.StringProperty()
    code = ndb.StringProperty()

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
        template = env.get_template('page.html')
        self.response.out.write(template.render())

    def post(self):
        information_key = ndb.Key('Information', self.request.get('name'))
        information = information_key.get()
        if not information:

            code = ""
            kids = ""
            job = ""
            family = ""

            if self.request.get("code") == "dog":
                code = "The Dog Century"
            if self.request.get("code") == "daycare":
                code = "Daycare Playcare"
            if self.request.get("code") == "shop":
                code = "Whole Veggies"

            if self.request.get("kids") == "yes":
                kids = "Yes"
            if self.request.get("kids") == "no":
                kids = "No"

            if self.request.get("job") == "yes":
                job = "Yes"
            if self.request.get("job") == "no":
                job = "No"

            if self.request.get("family") == "yes":
                family = "Yes"
            if self.request.get("family") == "no":
                family = "No"

            information = Information(code = code,
                                        kids = kids,
                                        job = job,
                                        family = family,
                                        name = self.request.get('name'),
                                        street = self.request.get('street'),
                                        city = self.request.get('city'),
                                        state = self.request.get('state'),
                                        zipcode = long(self.request.get('zipcode')),
                                        phonenumber = long(self.request.get('number')),
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
        self.redirect('/companion')



app = webapp2.WSGIApplication([
        ('/', Begin),
        ('/begin2', Begin2),
        ('/dark', Creepy),
        ('/sunshine', Sunshine),
        ('/tree', Tree),
        ('/poro', InformationPage),
        ('/companion', Companion),
], debug = True)
