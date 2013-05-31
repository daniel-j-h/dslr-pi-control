TODO
====

$ grep -n 'XXX'


Functionality
-------------

There's already a snapshot() and timelapse() function, but I wanted to first get a thumbnail back.
This is kind of tricky, because we have to create a user-specific tempdir, download the image, send-file it to the user and clean up afterwards.


gphoto2 calls
-------------

* --capture-image-and-download

* --get-config CONFIGENTRY
* --set-config-index CONFIGENTRY=CONFIGINDEX

* --get-thumbnail 1-5
