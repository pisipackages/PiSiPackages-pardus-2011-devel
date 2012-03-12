#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="Imaging-%s" % get.srcVERSION()

def install():
    pythonmodules.install()

    shelltools.cd("Sane")
    pythonmodules.install()
    shelltools.cd("..")

    for header in ["Imaging.h","ImPlatform.h"]:
        pisitools.insinto("/usr/include/%s" % get.curPYTHON(), "libImaging/%s" % header)

    pisitools.dodoc("README")

