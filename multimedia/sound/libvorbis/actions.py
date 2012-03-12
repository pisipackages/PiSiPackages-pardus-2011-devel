#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    # sanitize flags
    pisitools.dosed("configure", "-mno-ieee-fp")
    pisitools.dosed("configure", "-mfused-madd")
    pisitools.dosed("configure", "-mcpu=750")
    pisitools.dosed("configure", "-O20")

    options = "--disable-static"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc")

    pisitools.dodoc("AUTHORS", "README", "todo.txt", "doc/*.txt")
    pisitools.dohtml("doc/*")
