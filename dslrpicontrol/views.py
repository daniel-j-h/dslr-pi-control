# -*- coding: utf-8 -*-

from flask import render_template

from dslrpicontrol import app
from dslrpicontrol.decorators import templated


@app.route('/')
@templated('baselayout.html')
def index():
    return dict(msg='Hello there!')


# vim: set tabstop=4 shiftwidth=4 expandtab:
