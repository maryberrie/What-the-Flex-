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
