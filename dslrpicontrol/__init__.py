# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)

import dslrpicontrol.views
import dslrpicontrol.errorhandlers


# vim: set tabstop=4 shiftwidth=4 expandtab:
