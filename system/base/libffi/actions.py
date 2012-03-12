#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "--disable-static"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --includedir=/emul32/include \
                     --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def check():
    # Needs dejagnu package
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog*", "LICENSE", "README*")

    # Remove duplicated header files
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/lib32/%s" % get.srcDIR())
