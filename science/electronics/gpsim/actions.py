#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.sym(".", "m4")
    autotools.autoreconf("-fvi")
    autotools.configure("--enable-shared --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING", "NEWS", "PROCESSORS", "README", "README.*", "TODO")
    pisitools.dodoc("doc/gpsim.*")
