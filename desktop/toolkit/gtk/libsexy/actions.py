#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS")
