# -*- coding: utf-8 -*-

import re
from subprocess import check_output, CalledProcessError
from flask import flash

from dslrpicontrol import app


def prepared_call(arguments):
    command = ['gphoto2', '--quiet']
    command.extend(arguments)

    ret = [""]

    try:
        ret = check_output(command).splitlines()
    except CalledProcessError as e:
        app.logger.exception(e)
        flash(u'Process returned with unexpected value', 'danger')
    except EnvironmentError as e:
        app.logger.exception(e)
        flash(u'Unable to call process', 'danger')

    return ret


def auto_detect():
    ret = prepared_call(['--auto-detect'])

    # filter separating line
    ret = [x.strip() for x in ret if not x.startswith('---') and not x.endswith('---')]

    # get (model, port) from smth. like "fst   snd   "
    ret = [re.search(r'^(?P<model>.+?)(\s+)(?P<port>.+$)', x.strip()).group('model', 'port') for x in ret]

    # transform to {model=x[0], port=x[1]}
    ret = [dict(model=x[0], port=x[1]) for x in ret]

    return ret


def abilities():
    return prepared_call(['--abilities'])


def list_config():
    return prepared_call(['--list-config'])


def storage_info():
    return prepared_call(['--storage-info'])


def summary():
    return prepared_call(['--summary'])


# vim: set tabstop=4 shiftwidth=4 expandtab:
