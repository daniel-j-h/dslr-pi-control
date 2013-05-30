# -*- coding: utf-8 -*-

from flask import flash, redirect, url_for

from dslrpicontrol import app
from dslrpicontrol.decorators import templated
from dslrpicontrol.models import auto_detect, abilities, storage_info, summary, reset_usb


@app.route('/')
@templated('baselayout.html')
def index():
    return redirect(url_for('camera'))


@app.route('/camera')
@templated('camera.html')
def camera():
    return dict(auto_detect=auto_detect(), abilities=abilities(), storage_info=storage_info(), summary=summary())

@app.route('/camera/autodetect')
@templated('cameraproperties.html')
def camera_auto_detect():
    return dict(caption='Auto detection', headers=['Key', 'Value'], properties=[dict(a='b', c='d'), dict(e='f', g='h')])


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


@app.route('/reset')
def reset():
    reset_usb()
    return redirect(url_for('timelapse'))


# vim: set tabstop=4 shiftwidth=4 expandtab:
