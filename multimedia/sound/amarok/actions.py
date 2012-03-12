#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DWITH_Ipod=ON -DWITH_IPOD=ON")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("AUTHORS", "README", "COPYING", "ChangeLog")
