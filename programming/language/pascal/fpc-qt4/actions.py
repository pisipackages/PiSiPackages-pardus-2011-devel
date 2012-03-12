#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

if get.ARCH() == "i686":
    WorkDir="bin-qt4pas-V2.1_Qt4.5.3"

    def install_lib():
        pisitools.dolib("libQt4Pas.so.5.2.1")
        pisitools.dosym("libQt4Pas.so.5.2.1", "/usr/lib/libQt4Pas.so")
        pisitools.dosym("libQt4Pas.so.5.2.1", "/usr/lib/libQt4Pas.so.5")
        pisitools.dosym("libQt4Pas.so.5.2.1", "/usr/lib/libQt4Pas.so.5.2")

else:
    def setup():
        shelltools.system("qmake PREFIX=%s/usr" % get.installDIR())

    def build():
        autotools.make()

    def install_lib():
        autotools.rawInstall("DESTDIR=%s INSTALL_ROOT=%s" %(get.installDIR(), get.installDIR()))

def install():
    install_lib()

    pisitools.dodoc("COPYING.TXT", "README.TXT")
