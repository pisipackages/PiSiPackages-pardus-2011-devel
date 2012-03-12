#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --x11dir=/usr/share/fonts/terminus")

def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install" % get.installDIR())
    autotools.make("DESTDIR=%s fontdir" % get.installDIR())

    pisitools.dosym("../conf.avail/63-terminus-fonts-fontconfig.conf", "/etc/fonts/conf.d/63-terminus-fonts-fontconfig.conf")

    pisitools.dodoc("README")
