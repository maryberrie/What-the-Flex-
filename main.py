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
    zipcode = ndb.StringProperty()
    phonenumber = ndb.StringProperty()
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

class Companion2(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('2companionsunshine.html')
        self.response.out.write(template.render())

class Waterfall(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('3waterfall.html')
        self.response.out.write(template.render())

class House(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('3house.html')
        self.response.out.write(template.render())

class Boat(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('4boat.html')
        self.response.out.write(template.render())

class NoBoat(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('4noboat.html')
        self.response.out.write(template.render())

class Investigate(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('4investigate.html')
        self.response.out.write(template.render())

class NoInvestigate(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('4noinvestigate.html')
        self.response.out.write(template.render())

class Island(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('5island.html')
        self.response.out.write(template.render())

class NoIsland(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('5noisland.html')
        self.response.out.write(template.render())

class Cave(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('5cave.html')
        self.response.out.write(template.render())

class Field(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('5field.html')
        self.response.out.write(template.render())

class DrinkEscape(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('6drinkescape.html')
        self.response.out.write(template.render())

class Stone(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('6stone.html')
        self.response.out.write(template.render())

class NoStone(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('6nostone.html')
        self.response.out.write(template.render())

class Stick(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('7stickattack.html')
        self.response.out.write(template.render())

class AttackEscape(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('7attackescape.html')
        self.response.out.write(template.render())

class PowerEscape(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('7powerescape.html')
        self.response.out.write(template.render())

class StickEscape(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('8stickescape.html')
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
                                        zipcode = self.request.get('zipcode'),
                                        phonenumber = self.request.get('number'),
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

class InformationPage2(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('page2.html')
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
                                        zipcode = self.request.get('zipcode'),
                                        phonenumber = self.request.get('number'),
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
        self.redirect('/companionsunshine')


app = webapp2.WSGIApplication([
        ('/', Begin),
        ('/begin2', Begin2),
        ('/dark', Creepy),
        ('/sunshine', Sunshine),
        ('/tree', Tree),
        ('/poro', InformationPage),
        ('/poro2', InformationPage2),
        ('/companion', Companion),
        ('/companionsunshine', Companion2),
        ('/waterfall', Waterfall),
        ('/house', House),
        ('/boat', Boat),
        ('/noboat', NoBoat),
        ('/investigate', Investigate),
        ('/noinvestigate', NoInvestigate),
        ('/island', Island),
        ('/noisland', NoIsland),
        ('/cave', Cave),
        ('/field', Field),
        ('/drinkescape', DrinkEscape),
        ('/stone', Stone),
        ('/nostone', NoStone),
        ('/stick', Stick),
        ('/attackescape', AttackEscape),
        ('/powerescape', PowerEscape),
        ('/stickescape', StickEscape),
], debug = True)
