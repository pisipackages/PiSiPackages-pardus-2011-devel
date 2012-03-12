#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."

def setup():
    shelltools.makedirs("%s/lib" % get.workDIR())

    jarlist = ["dbus", "mina-core", "zemberek-cekirdek", "zemberek-tr"]

    for jars in jarlist:
        print ("%s/%s.jar" % ("/usr/share/java", jars))
        shelltools.sym("%s/%s.jar" % ("/usr/share/java", jars), "%s/lib/%s.jar" % (get.workDIR(), jars))

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/etc", "dist/config/conf.ini", "zemberek-server.ini")
    pisitools.insinto("/etc/dbus-1/system.d", "dist/config/zemberek-server.conf")
    pisitools.insinto("/usr/share/java", "dist/zemberek-server-%s.jar" % get.srcVERSION())
    pisitools.dosym("zemberek-server-%s.jar" % get.srcVERSION(), "/usr/share/java/zemberek-server.jar")

    pisitools.dodoc("dist/lisanslar/zemberek-licence.txt")

