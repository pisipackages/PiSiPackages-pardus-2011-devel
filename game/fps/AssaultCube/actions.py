#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

#WorkDir = "AssaultCube_v%s" % get.srcVERSION()
WorkDir = "AC%s" % get.srcVERSION()

datasources = ["bot", "config", "packages"]
src = "source/src"
datadir = "/usr/share/AssaultCube"
mapdir = "%s/packages/maps" % datadir

shelltools.export("LC_ALL", "C")

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    pisitools.dosed("%s/Makefile" % src, "STRIP=strip", "STRIP=")

    for d in datasources:
        fixperms(d)

    fixperms("docs")

    # for nowin32 patch
    shelltools.cd("source/enet")
    autotools.autoreconf("-vfi")

def build():
    shelltools.cd(src)
    autotools.make('CXXOPTFLAGS="%s -fomit-frame-pointer" -j1' % get.CXXFLAGS())

def install():
    pisitools.dodir(datadir)
    for d in datasources:
        shelltools.copytree(d, "%s/%s" % (get.installDIR(), datadir))

    for f in ["ac_client", "ac_server"]:
        pisitools.dobin("source/src/%s" % f, datadir)

    # make official maps reachable in client, see bug #11276
    for i in shelltools.ls("%s/%s/official" % (get.installDIR(), mapdir)):
        pisitools.domove("%s/official/%s" % (mapdir, i), mapdir)

    pisitools.removeDir("%s/official" % mapdir)
    pisitools.dosym("./", "%s/official" % mapdir)

    pisitools.dodoc("source/*.txt", "README.html", "icon.ico")
    shelltools.copytree("docs", "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME()))

