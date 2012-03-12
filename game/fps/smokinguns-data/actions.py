#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

import os

WorkDir = "Smokin\' Guns"

NoStrip = "/"

datadir = "/usr/share/smokinguns"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    for dir in ["baseq3", "smokinguns"]:
        fixperms(dir)
        pisitools.insinto(datadir, dir)

    pisitools.dohtml("manual/*")
    pisitools.dodoc("*.txt")
