# -*- coding: utf-8 -*-

from dslrpicontrol import app


@app.errorhandler(404)
def page_not_found(e):
    return '404 - not found', 404


@app.errorhandler(403)
def page_forbidden(e):
    return '403 - forbidden', 403


@app.errorhandler(410)
def page_gone(e):
    return '410 - gone', 410


@app.errorhandler(500)
def not_found(e):
    return '500 - internal server error', 500


# vim: set tabstop=4 shiftwidth=4 expandtab:
