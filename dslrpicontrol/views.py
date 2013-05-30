# -*- coding: utf-8 -*-

from flask import render_template, flash

from dslrpicontrol import app
from dslrpicontrol.decorators import templated


@app.route('/')
@templated('baselayout.html')
def index():
    return dict(heading='pi-control', subtext='it\'s awesome!')


@app.route('/camera')
@templated('baselayout.html')
def camera():
    flash(u'camera alert', 'danger')
    flash(u'2nd alert')
    return None


@app.route('/capture')
@templated('baselayout.html')
def capture():
    flash(u'capture alert', 'success')
    return None


@app.route('/timelapse')
@templated('baselayout.html')
def timelapse():
    flash(u'timelapse alert', 'info')
    return None


# vim: set tabstop=4 shiftwidth=4 expandtab:
