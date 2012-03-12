#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--without-webkit \
                         --disable-gtk-doc \
                         --disable-altivec \
                         --enable-gimp-remote \
                         --enable-python \
                         --enable-mmx \
                         --enable-sse \
                         --enable-mp \
                         --with-linux-input \
                         --with-gnomevfs \
                         --with-poppler \
                         --with-libjpeg \
                         --with-libexif \
                         --with-librsvg \
                         --with-libtiff \
                         --with-libmng \
                         --with-libpng \
                         --with-webkit \
                         --with-lcms \
                         --with-alsa \
                         --with-dbus \
                         --with-aa \
                         --with-x")

    # Add illustrator and other mime types
    pisitools.dosed("desktop/gimp.desktop.in", "^MimeType=application/postscript;application/pdf;(.*)$",
                    "MimeType=\\1;image/x-sun-raster;image/x-gray;image/x-pcx;image/jpg;image/x-bmp;image/pjpeg;image/x-png;application/illustrator;")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README", "INSTALL", "LICENSE")
