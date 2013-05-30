# -*- coding: utf-8 -*-

import re
from subprocess import check_output, CalledProcessError
from flask import flash

from dslrpicontrol import app


def prepared_call(arguments):
    command = ['gphoto2', '--quiet']
    command.extend(arguments)

    return check_output(command).splitlines()


def auto_detect():
    try:
        ret = prepared_call(['--auto-detect'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Auto-detecting failed', 'danger')
        return []

    # nothing detected
    if (len(ret) == 2): return []

    # filter: separating line
    ret = [x for x in ret if not x.startswith('---') and not x.endswith('---')]
    # map: transform to [(model, port), ...] from smth. like: ["model   port  ", ...]
    ret = [re.search(r'^(?P<model>.+?)(\s+)(?P<port>.+$)', x).group('model', 'port') for x in ret]
    # map: transform to [{model=x[0], port=x[1]}, ...]
    return [dict(model=x[0].strip(), port=x[1].strip()) for x in ret]


def abilities():
    try:
        ret = prepared_call(['--abilities'])
    except (CalledProcessError, EnvironmentError) as e:
        app.logger.exception(e)
        flash(u'Checking abilities failed', 'danger')
        return []

    # map: transform to [(feature, support), ...] from smth. like: ["feature  : support  ", ...]
    ret = [re.search(r'^(?P<feature>.*?)(\s*:\s*)(?P<support>.*$)', x).group('feature', 'support') for x in ret]
    # map: transform to [{feature=x[0], suppport=x[1]}, ...]
    return [dict(feature=x[0].strip(), support=x[1].strip()) for x in ret]


def list_config():
    return prepared_call(['--list-config'])


def storage_info():
    return prepared_call(['--storage-info'])


def summary():
    return prepared_call(['--summary'])


# vim: set tabstop=4 shiftwidth=4 expandtab:
