# -*- coding: utf-8 -*-

import re
from subprocess import check_call, check_output, CalledProcessError
from flask import flash

from dslrpicontrol import app


def prepared_call(arguments):
    command = ['gphoto2', '--quiet']
    command.extend(arguments)

    return check_output(command).splitlines()


def auto_detect():
    try:
        # XXX: does not throw if no camera available; this behavior is different from all other gphoto2 calls
        ret = prepared_call(['--auto-detect'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Auto-detection request failed', 'danger')
        return []

    # nothing detected, only header and separation line
    if (len(ret) == 2): return []

    # header
    ret.pop(0)
    # separating line
    ret.pop(0)

    # map: transform to [(model, port), ...] from smth. like: ["model   port  ", ...]
    ret = [re.search(r'^(?P<model>.+?)(\s+)(?P<port>.+$)', x.strip()).group('model', 'port') for x in ret]
    # map: transform to [{model=x[0], port=x[1]}, ...]
    return [dict(model=x[0], port=x[1]) for x in ret]


def abilities():
    try:
        ret = prepared_call(['--abilities'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Ability request failed', 'danger')
        return []

    # filter: empty lines
    ret = filter(lambda x: not len(x) == 0, ret)
    # map: transform to [(feature, support), ...] from smth. like: ["feature  : support  ", ...]
    ret = [re.search(r'^(?P<feature>.*?)(\s*:\s*)(?P<support>.*$)', x.strip()).group('feature', 'support') for x in ret]
    # map: transform to [{feature=x[0], suppport=x[1]}, ...]
    return [dict(feature=x[0], support=x[1]) for x in ret]


def storage_info():
    try:
        ret = prepared_call(['--storage-info'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Storage information request failed', 'danger')
        return []

    # filter: group name
    ret = filter(lambda x: not x.startswith('[') and not x.endswith(']') and not len(x) == 0, ret)
    # map: transform to (property, value) from smth. like: ["property=value", ...]
    ret = [re.search(r'^(?P<property>.+?)(=)(?P<value>.+$)', x.strip()).group('property', 'value') for x in ret]
    # map: transform to [{property=x[0], value=x[1]}, ...]
    return [dict(property=x[0], value=x[1]) for x in ret]


def summary():
    try:
        ret = prepared_call(['--summary'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Summary request failed', 'danger')
        return []

    # filter: empty lines
    ret = filter(lambda x: not len(x) == 0, ret)
    # map: transform to [(property, value), ...] from smth. like: ["property:value  ", ...]
    print(ret)
    ret = [re.search(r'^(?P<property>.*?)(\s*:\s*)(?P<value>.*$)', x.strip()).group('property', 'value') for x in ret]
    # map: transform to [{feature=x[0], suppport=x[1]}, ...]
    return [dict(property=x[0], value=x[1]) for x in ret]


def list_config():
    return prepared_call(['--list-config'])


def reset_usb():
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


# vim: set tabstop=4 shiftwidth=4 expandtab:
