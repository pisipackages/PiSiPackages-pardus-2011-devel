#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "djvulibre-%s" % get.srcVERSION()

def setup():
    autotools.aclocal("-I config")
    autotools.autoconf("-f")

    autotools.configure("--enable-threads \
                         --disable-desktopfiles \
                         --enable-xmltools \
                         --enable-i18n \
                         --with-jpeg \
                         --with-tiff")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/mime/packages", "desktopfiles/djvulibre-mime.xml")

    for size in ["22", "32", "48", "64"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/mimetypes" %(size, size), "desktopfiles/hi%s-djvu.png" % size, "image-vnd.djvu.png")

    pisitools.dodoc("README", "TODO", "NEWS")
