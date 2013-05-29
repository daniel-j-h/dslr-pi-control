# -*- coding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

app.config.from_pyfile('application.cfg', silent=True)


@app.route('/')
def index():
    return 'dslr-pi-control %s' % app.config['SECRET_KEY']



# vim: set tabstop=4 shiftwidth=4 expandtab:
