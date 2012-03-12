#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "iniparser%s" % get.srcVERSION()

def build():
    autotools.make("CC=%s CFLAGS='%s -fPIC' LDFLAGS='%s'" % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dolib_so("libiniparser.so.0")
    pisitools.dosym("libiniparser.so.0", "/usr/lib/libiniparser.so")

    pisitools.dodir("/usr/include")
    pisitools.insinto("/usr/include", "src/*.h")

    pisitools.dodoc("README", "AUTHORS", "LICENSE")
