#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("ant clean")

def build():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java", "dist/*.jar")

    pisitools.dodir(get.docDIR())
    shelltools.copytree("dist/docs", "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME()))
    pisitools.dodoc("LICENSE.txt")

