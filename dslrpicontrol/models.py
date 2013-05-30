# -*- coding: utf-8 -*-

import re
from subprocess import check_call, check_output, CalledProcessError
from collections import OrderedDict

from flask import flash

from dslrpicontrol import app, cache


def prepared_call(arguments):
    command = ['gphoto2', '--quiet']
    command.extend(arguments)

    return check_output(command).splitlines()


def tup_lst_to_dict(tup_lst):
    # OrderedDict (think: tree-based map) preserves ordering;
    # using it here is enough for all our code to magically do The Right Thing
    to_dict = lambda lst: OrderedDict(lst)
    strip_tup = lambda (a, b): (a.strip(), b.strip())

    return to_dict(map(strip_tup, tup_lst))


@cache.cached(timeout=60 * 15, key_prefix='auto_detect')
def auto_detect():
    try:
        # XXX: does not throw if no camera is available; this behavior is different from all other gphoto2 calls
        ret = prepared_call(['--auto-detect'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Auto-detection request failed', 'danger')
        return dict()

    # nothing detected, only header and separation line
    if (len(ret) == 2):
        flash(u'Auto-detection was not able to detect your camera', 'info')
        return dict()

    # remove header and separating line
    ret.pop(0)
    ret.pop(0)

    # map: transform to [(model, port), ...] from smth. like: ['model   port  ', ...]
    ret = [re.search(r'^(?P<model>.+)(\s+)(?P<port>.+$)', x.strip()).group('model', 'port') for x in ret]

    return tup_lst_to_dict(ret)


@cache.cached(timeout=60 * 15, key_prefix='abilities')
def abilities():
    try:
        ret = prepared_call(['--abilities'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Ability request failed', 'danger')
        return dict()

    # filter: empty lines
    ret = filter(lambda x: not len(x) == 0, ret)
    # map: transform to [(feature, support), ...] from smth. like: ['feature  : support  ', ...]
    ret = [re.search(r'^(?P<feature>.*)(\s*:\s*)(?P<support>.*$)', x.strip()).group('feature', 'support') for x in ret]

    return tup_lst_to_dict(ret)


@cache.cached(timeout=60 * 15, key_prefix='storage_info')
def storage_info():
    try:
        ret = prepared_call(['--storage-info'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Storage information request failed', 'danger')
        return dict()

    # filter: group name
    ret = filter(lambda x: not x.startswith('[') and not x.endswith(']') and not len(x) == 0, ret)
    # map: transform to (property, value) from smth. like: ['property=value', ...]
    ret = [re.search(r'^(?P<property>.+)(=)(?P<value>.+$)', x.strip()).group('property', 'value') for x in ret]

    return tup_lst_to_dict(ret)


def reset_usb():
    cache.clear()

    try:
        ret = check_output(['lsusb']).splitlines()
        ret = filter(lambda x: app.config.get('CAMERA', 'Nikon') in x, ret)

        if len(ret) < 1:
            app.logger.error('usbreset found no camera')
            flash(u'USB reset request found no camera, not resetting', 'danger')
            return

        if len(ret) > 1:
            app.logger.warning('usbreset found more than one camera')
            flash(u'USB reset request found more than one camera, resetting all', 'info')

        ret = [re.search(r'Bus (?P<bus>\d{3}?) Device (?P<device>\d{3})', x.strip()).group('bus', 'device') for x in ret]
        map(lambda x: check_call(['usbreset', '/dev/bus/usb/{0}/{1}'.format(x[0], x[1])]), ret)

        flash(u'USB reset request was successfull', 'success')
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'USB reset request failed', 'danger')


def list_config():
    try:
        ret = prepared_call(['--list-config'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Configuration request failed', 'danger')
        return dict()

    # XXX
    ret = [(x, 'undefined') for x in ret]

    return tup_lst_to_dict(ret)


def timelapse(frames=1, interval=10):
    try:
        check_call(['--frames', frames, '--interval', interval, '--capture-image'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Timelapse request failed')
        return


def snapshot():
    try:
        check_call(['--capture-image'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Snaphot request failed')
        return


# vim: set tabstop=4 shiftwidth=4 expandtab:
