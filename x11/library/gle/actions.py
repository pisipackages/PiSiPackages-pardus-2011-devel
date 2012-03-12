#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gle-graphics-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-x \
                         --with-rpath=no \
                         --with-qt=/usr/lib/qt4")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/lib/pkgconfig")

    pisitools.dodoc("README.txt", "LICENSE.txt")
