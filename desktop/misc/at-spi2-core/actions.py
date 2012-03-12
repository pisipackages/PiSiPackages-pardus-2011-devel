#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --disable-xevie \
                         --disable-relocate \
                         --libexecdir=/usr/libexec/at-spi2 \
                         --with-dbus-daemondir=/usr/bin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/etc")
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS")
