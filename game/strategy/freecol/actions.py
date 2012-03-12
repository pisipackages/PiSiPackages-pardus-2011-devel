#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = 'freecol'

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/freecol", "FreeCol.jar")
    pisitools.insinto("/usr/share/freecol/data", "data/*")
    pisitools.insinto("/usr/share/freecol/jars", "jars/*")

    pisitools.doman("packaging/debian/freecol.6")
    pisitools.dodoc("packaging/common/README", "packaging/common/COPYING")
