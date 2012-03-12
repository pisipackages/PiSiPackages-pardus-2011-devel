#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CXXFLAGS", '%s -DEXPDATADIR=\\\"/usr/share/abuse\\\"' % get.CXXFLAGS())
    autotools.configure("--datadir=/usr/share/abuse --with-x")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "TODO")
