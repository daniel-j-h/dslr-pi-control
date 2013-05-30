# -*- coding: utf-8 -*-

from flask import redirect, url_for

from dslrpicontrol import app
from dslrpicontrol.decorators import templated
from dslrpicontrol.models import auto_detect, abilities, storage_info, reset_usb, list_config#, timelapse, snapshot


@app.route('/')
def index():
    return redirect(url_for('camera'))


# camera handlers
@app.route('/camera/')
def camera():
    return redirect(url_for('camera_autodetect'))


@app.route('/camera/autodetect')
@templated('camera.html')
def camera_autodetect():
    return dict(caption='Auto detection', header=dict(key='Model', value='Port'), properties=auto_detect())


@app.route('/camera/abilities')
@templated('camera.html')
def camera_abilities():
    return dict(caption='Abilities', header=dict(key='Features', value='Support'), properties=abilities())


@app.route('/camera/storage')
@templated('camera.html')
def camera_storage():
    return dict(caption='Storage information', header=dict(key='Property', value='Value'), properties=storage_info())


@app.route('/camera/settings')
@templated('camera.html')
def camera_settings():
    return dict(caption='Settings', header=dict(key='Property', value='Value'), properties=list_config())


@app.route('/camera/reset')
def camera_reset():
    reset_usb()
    return redirect(url_for('camera'))


# capture handlers
@app.route('/capture/')
def capture():
    return redirect(url_for('capture_image'))


@app.route('/capture/image')
@templated('capture.html')
def capture_image():
    return dict(caption='Capture image')


@app.route('/capture/timelapse')
@templated('capture.html')
def capture_timelapse():
    return dict(caption='Timelapse')


# vim: set tabstop=4 shiftwidth=4 expandtab:
