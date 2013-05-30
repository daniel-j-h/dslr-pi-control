# -*- coding: utf-8 -*-

from flask import flash, redirect, url_for

from dslrpicontrol import app
from dslrpicontrol.decorators import templated
from dslrpicontrol.models import auto_detect, abilities, storage_info, reset_usb


@app.route('/')
def index(): return redirect(url_for('camera'))

@app.route('/camera/')
def camera(): return redirect(url_for('camera_autodetect'))

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

@app.route('/camera/reset')
def camera_reset():
    reset_usb()
    return redirect(url_for('camera'))



@app.route('/capture/')
def capture(): return redirect(url_for('capture_image'))

@app.route('/capture/image')
@templated('capture.html')
def capture_image():
    return None

@app.route('/capture/video')
@templated('capture.html')
def capture_video():
    return None

@app.route('/capture/audio')
@templated('capture.html')
def capture_audio():
    return None



@app.route('/timelapse/')
def timelapse(): return redirect(url_for('timelapse_timer'))

@app.route('/timelapse/timer')
@templated('timelapse.html')
def timelapse_timer():
    return None

@app.route('/timelapse/countdown')
@templated('timelapse.html')
def timelapse_countdown():
    return None


# vim: set tabstop=4 shiftwidth=4 expandtab:
