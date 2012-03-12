#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #install HAL file for portable audio players
    pisitools.insinto("/usr/share/hal/fdi/information/10freedesktop", "libmtp.fdi", "10-usb-music-players-libmtp.fdi")

    #rename UDEV rules
    pisitools.rename("/lib/udev/rules.d/libmtp.rules", "60-libmtp.rules")

    pisitools.removeDir("/usr/share/doc/libmtp-*")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "AUTHORS", "TODO")
