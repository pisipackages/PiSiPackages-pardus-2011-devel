#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CXXFLAGS", "%s -I/usr/include/clanlib-0.6.5" % get.CXXFLAGS())
    shelltools.export("LDFLAGS", "%s -L/usr/lib/clanlib-0.6.5" % get.LDFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    shelltools.export("HOME", get.curDIR())
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "IDEAS", "QUOTES", "README")
