#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get


WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))

def setup():
    shelltools.sym(".", "m4")
    shelltools.export("CFLAGS", "%s -DDRV_RAW" % get.CFLAGS())

    autotools.autoreconf("-vfi -Im4")
    libtools.gnuconfig_update()

    options = "--disable-esd \
               --disable-af \
               --disable-alsa \
               --enable-oss \
               --disable-static"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --bindir=/emul32/bin"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("CFLAGS", "%s -DDRV_RAW -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO")
    pisitools.dohtml("docs/*.html")

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
