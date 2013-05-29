dslr-pi-control
---------------

Having fun with the Nikon D3100 dslr, using the browser. Mobile friendly and totally awesome!

Tested on Chrome, Nexus 4 smartphone, Nexus 7 tablet.


What it looks like
------------------

IMG


Flask setup
-----------

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt


Python bindings for libgphoto2
------------------------------

Get the bindings from https://github.com/alexdu/piggyphoto

Just throw the piggyphoto subdirectory into your env's site-packages directory.

    git clone --depth 0 git://github.com/alexdu/piggyphoto.git
    mv piggyphoto/piggyphoto env/lib/python2.7/site-packages/


Buggy USB workaround
--------------------

See the usbreset code in the utils directory.

    gcc usbreset.c -static -o usbreset
    strip --strip-unneeded usbreset
    mv usbreset /usr/local/bin/


Start the server
----------------

If you want to be fancy, you can install a web server (e.g. lighttpd, nginx) and let the Flask app communicate (e.g. FastCGI, uWSGI) with it using WSGI.

Otherwise, just use the Flask server:

    ./app
