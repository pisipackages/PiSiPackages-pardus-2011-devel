#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("make/linux/Makefile", "CXXFLAGS=", "CXXFLAGS+=")

def build():
    shelltools.cd("make/linux")
    autotools.make("PREFIX=/usr \
                   LIBEBML_INCLUDE_DIR=/usr/include/ebml \
                   LIBEBML_LIB_DIR=/usr/lib")

def install():
    shelltools.cd("make/linux")
    autotools.install("libdir=%s/usr/lib" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("../../ChangeLog")
