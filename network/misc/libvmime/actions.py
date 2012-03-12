#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-rpath \
                         --disable-static \
                         --disable-sasl")

    flagorderrx = (r"(\\\$deplibs \\\$postdep_objects) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *flagorderrx)

def build():
    autotools.make('CFLAGS="%s" CXXFLAGS="%s"' % (get.CFLAGS(), get.CXXFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
