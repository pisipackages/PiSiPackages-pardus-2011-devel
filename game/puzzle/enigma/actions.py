#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    for i in ["NEWS", "ChangeLog"]:
        shelltools.touch(i)

    autotools.autoreconf("-f -i -Wno-portability")
    autotools.configure("--disable-dependency-tracking \
                         --enable-optimize \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # we will use our desktop file
    pisitools.remove("/usr/share/applications/enigma.desktop")

    pisitools.dodoc("ACKNOWLEDGEMENTS", "AUTHORS", "CHANGES", "README", "doc/HACKING")
    pisitools.dohtml("doc/*")
    pisitools.doman("doc/enigma.6")
