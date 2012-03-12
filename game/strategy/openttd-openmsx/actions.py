#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "openmsx-%s-source" % get.srcVERSION()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/share/openttd/gm", "openmsx-%s/*.mid" % get.srcVERSION())
    pisitools.insinto("/usr/share/openttd/gm", "openmsx-%s/openmsx.obm" % get.srcVERSION())

    pisitools.dodoc("openmsx-%s/*.txt" % get.srcVERSION())
