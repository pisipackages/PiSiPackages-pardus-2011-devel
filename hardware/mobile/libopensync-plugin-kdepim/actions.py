#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    # Fix QMetaType include error
    autotools.make("CXXFLAGS='%s -I/usr/include/QtCore'" % get.CXXFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING")
