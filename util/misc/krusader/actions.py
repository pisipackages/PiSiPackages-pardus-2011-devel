#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

NoStrip=["/usr/share", "/usr/man"]
WorkDir="krusader-%s" % get.srcVERSION().replace("_","-")
shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
    pisitools.dosym("/usr/share/icons/hicolor/48x48/apps/krusader_user.png", "/usr/share/icons/hicolor/48x48/apps/krusader.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "FAQ")
