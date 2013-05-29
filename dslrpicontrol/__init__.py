# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('development.cfg')
#app.config.from_pyfile('production.cfg')


import dslrpicontrol.views
import dslrpicontrol.errorhandlers

if app.debug is not True:
    import dslrpicontrol.loggers


# vim: set tabstop=4 shiftwidth=4 expandtab:
