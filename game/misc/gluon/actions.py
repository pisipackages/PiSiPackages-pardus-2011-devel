#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

WorkDir="gluon-gluon"
shelltools.export("HOME", get.workDIR())

def setup():
    # ON if installing to /usr, OFF if otherwise
    pisitools.dosed("CMakeLists.txt", "CMake root\" OFF", "CMake root\" ON")
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
    pisitools.dodoc("COPYING")
