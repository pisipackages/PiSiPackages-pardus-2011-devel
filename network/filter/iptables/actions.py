#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sbindir=/sbin \
                         --libexecdir=/usr/lib \
                         --without-kernel \
                         --enable-devel \
                         --enable-libipq \
                         --enable-shared \
                         --enable-static")

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.insinto("/usr/include", "include/iptables.h")
    pisitools.insinto("/usr/include", "include/ip6tables.h")
    pisitools.insinto("/usr/include/libiptc", "include/libiptc/*.h")

    pisitools.dodir("/var/lib/iptables")
    pisitools.dodir("/etc/iptables")
