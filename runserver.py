#!env/bin/python
# -*- coding: utf-8 -*-

from dslrpicontrol import app


app.config['SECRET_KEY'] = 'your-secret-key'
app.run(host='0.0.0.0', port=8080, debug=True)


# vim: set tabstop=4 shiftwidth=4 expandtab:
