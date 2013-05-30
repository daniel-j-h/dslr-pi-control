# -*- coding: utf-8 -*-

from flask import flash, redirect, url_for

from dslrpicontrol import app
from dslrpicontrol.decorators import templated
from dslrpicontrol.models import auto_detect


@app.route('/')
@templated('baselayout.html')
def index():
    return redirect(url_for('camera'))


@app.route('/camera')
@templated('camera.html')
def camera():
    return dict(auto_detect=auto_detect(), abilities=abilities())


@app.route('/capture')
@templated('capture.html')
def capture():
    flash(u'capture alert', 'success')
    return None


@app.route('/timelapse')
@templated('timelapse.html')
def timelapse():
    flash(u'timelapse alert', 'info')
    return None


# vim: set tabstop=4 shiftwidth=4 expandtab:
