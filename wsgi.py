import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

from mainweb import index
from bs4 import BeautifulSoup
import bottle
from bottle import route, get, template, static_file, request


application = bottle.default_app()
