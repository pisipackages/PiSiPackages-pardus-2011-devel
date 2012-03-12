#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME",get.workDIR())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-rpath \
                         --disable-integration-wizard \
                         --disable-deprecated \
                         --with-spidermonkey=/usr/include/js/ \
                         --enable-watchdog")



def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "AUTHORS", "ABOUT-NLS", "NEWS", "COPYING", "README")
