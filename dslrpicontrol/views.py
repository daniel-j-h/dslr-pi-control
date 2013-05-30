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
    return None


@app.route('/camera/autodetect')
@templated('camera.html')
def camera_autodetect():
    return dict(caption='Auto detection', headers=['Model', 'Port'], properties=auto_detect())


@app.route('/camera/abilities')
@templated('camera.html')
def camera_abilities():
    return dict(caption='Abilities', headers=['Features', 'Support'], properties=abilities())


@app.route('/camera/storage')
@templated('camera.html')
def camera_storage():
    return dict(caption='Storage information', headers=['Property', 'Value'], properties=storage_info())


@app.route('/camera/summary')
@templated('camera.html')
def camera_summary():
    return dict(caption='Summary', headers=['Property', 'Value'], properties=summary())


@app.route('/camera/reset')
def camera_reset():
    reset_usb()
    return redirect(url_for('camera'))




@app.route('/capture')
@templated('capture.html')
def capture():
    return None


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




@app.route('/timelapse')
@templated('timelapse.html')
def timelapse():
    return None


@app.route('/timelapse/timer')
@templated('timelapse.html')
def timelapse_timer():
    return None


@app.route('/timelapse/countdown')
@templated('timelapse.html')
def timelapse_countdown():
    return None


# vim: set tabstop=4 shiftwidth=4 expandtab:
