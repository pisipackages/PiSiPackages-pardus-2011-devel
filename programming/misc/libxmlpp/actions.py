#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libxml++-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --disable-examples \
                         --enable-dependency-tracking")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("docs/reference/html/*")

    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*")
    pisitools.removeDir("/usr/share/doc/libxml++-2.6")
