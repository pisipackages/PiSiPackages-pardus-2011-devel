#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--disable-debug \
                         --enable-static=no \
                         --includedir=/usr/include/libpisock \
                         --with-java=no \
                         --with-tcl=no \
                         --with-perl=yes \
                         --with-python=yes \
                         --with-libpng=/usr \
                         --with-readline=yes \
                         --with-bluez \
                         --enable-conduits \
                         --enable-threads \
                         --enable-libusb")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.copy("%s/usr/share/%s/udev*" % (get.installDIR(), get.srcNAME()), "%s/etc/udev/rules.d/" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "doc/README*", "doc/TODO", "NEWS", "AUTHORS")
