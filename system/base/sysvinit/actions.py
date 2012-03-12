#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sysvinit-%sdsf" % get.srcVERSION()

def build():
    autotools.make("-C src CC=\"%s\" CFLAGS=\"%s -D_GNU_SOURCE\" LCRYPT=\"-lcrypt\"" % (get.CC(), get.CFLAGS()))

def install():
    shelltools.cd("src")
    autotools.rawInstall("ROOT='%s' STRIP=/bin/true" % get.installDIR())

    pisitools.remove("/bin/pidof")
    pisitools.dosym("killall5", "/sbin/pidof")
