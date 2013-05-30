# -*- coding: utf-8 -*-

import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler

from dslrpicontrol import app


handler = RotatingFileHandler(app.config.get('LOG_FILE', 'dslr-pi-control.log'),
                              maxBytes=1024 * 1024 * 10, backupCount=5)

handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
handler.setLevel(logging.WARNING)

app.logger.addHandler(handler)


# vim: set tabstop=4 shiftwidth=4 expandtab:
