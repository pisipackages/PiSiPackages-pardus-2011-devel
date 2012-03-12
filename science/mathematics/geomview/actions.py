#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --with-pdfviewer=xdg-open \
                         --with-htmlbrowser=xdg-open")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "ChangeLog", "README", "NEWS", "AUTHORS")
