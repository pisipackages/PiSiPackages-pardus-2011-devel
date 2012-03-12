#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CFLAGS='%s -I.'" % get.CFLAGS())

def install():
    autotools.rawInstall("prefix=%s/usr libdir=%s/usr/lib" % (get.installDIR(), get.installDIR()))

    pisitools.remove("/usr/lib/*.a")
    pisitools.removeDir("/usr/share/man/man2")

    pisitools.dodoc("CHANGES", "DESIGN")
