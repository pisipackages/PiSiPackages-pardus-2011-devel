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
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-ipv6 \
                         --enable-bluetooth")

def build():
    autotools.make("all")
    autotools.make("shared")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    # it is needed for ppd etc.
    pisitools.insinto("/usr/include", "pcap-int.h")

    pisitools.dodoc("CHANGES", "CREDITS", "README*", "VERSION", "TODO")
