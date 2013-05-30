# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.cache import Cache


# inherits from Flask just so we're able to change some Jinja2 internals
class CustomFlask(Flask):
    jinja_options = dict(Flask.jinja_options, trim_blocks=True, lstrip_blocks=True, auto_reload=False)

app = CustomFlask(__name__, instance_relative_config=True)

app.config.from_pyfile('development.cfg')
#app.config.from_pyfile('production.cfg')


cache = Cache(app, config=app.config.get('CACHE_CONFIG', {'CACHE_TYPE' : 'simple'}))

with app.app_context():
    cache.clear()



import dslrpicontrol.views
import dslrpicontrol.models
import dslrpicontrol.errorhandlers

if app.debug is not True:
    import dslrpicontrol.loggers


# vim: set tabstop=4 shiftwidth=4 expandtab:
