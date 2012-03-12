#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.system("ant core")

def install():
    pisitools.insinto("/usr/share/java", "build/hamcrest-core-SNAPSHOT.jar", "hamcrest.jar")

    pisitools.dodoc("CHANGES.txt", "LICENSE.txt", "README.txt")
