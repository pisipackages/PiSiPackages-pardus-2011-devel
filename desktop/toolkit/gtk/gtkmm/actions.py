#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-demos \
                         --disable-docs")
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/gtkmm-2.4")
    pisitools.removeDir("/usr/share/devhelp")

    pisitools.dodoc("ChangeLog","COPYING", "PORTING", "NEWS", "README")
