#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cmt"

def build():
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CFLAGS())
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/ladspa", "plugins/*.so")
    pisitools.dodoc("README")
    pisitools.dohtml("doc/*")
