#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir = "."

def install():
    pisitools.insinto("/usr/share/fonts/nafees", "Nafees Naskh v2.01.ttf", "Nafees_Naskh.ttf")
    shelltools.chmod("%s/usr/share/fonts/nafees/*" % get.installDIR(), 0644)
