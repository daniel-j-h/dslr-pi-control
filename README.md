dslr-pi-control
---------------

Having fun with the Nikon D3100 dslr, using the browser. Mobile friendly and totally awesome!
Tested on Chrome, Nexus 4 smartphone, Nexus 7 tablet.

Note: This project serves primarily as a playground for me to refresh my knowledge about idiomatic Flask / Jinja2 setups.


What it looks like
------------------

IMG


Flask setup
-----------

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Note: requirements-devel.txt contains some additional code quality checkers.


gphoto2
-------

Unfortunately the libgphoto2 Python bindings are ugly, full of memory leaks and missing important functions.
The gphoto2 utility (subprocess) has to suffice. Get over it.


Buggy USB workaround
--------------------

See the usbreset code in the utils directory.

    gcc usbreset.c -static -o usbreset
    strip --strip-unneeded usbreset
    mv usbreset /usr/local/bin/


Start the server
----------------

If you want to be fancy, you can install a web server (e.g. lighttpd, nginx) and let the Flask app communicate (e.g. FastCGI, uWSGI) with it using WSGI. Please make sure to set DEBUG=False in the configuration as soon as you're not just playing around with it but using it e.g. on a public network.

Otherwise, just use the Flask server:

    ./runserver



Development
-----------

Try to keep the package clean.

    pep8 --show-source --max-line-length=120 dslrpicontrol
    pyflakes dslrpicontrol
