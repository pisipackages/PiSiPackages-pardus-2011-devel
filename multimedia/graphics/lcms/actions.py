#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #needed by mozilla patch
    autotools.autoreconf("-vfi")
    options = "--disable-dependency-tracking \
               --disable-static \
               --with-jpeg \
               --with-tiff \
               --with-zlib \
               --with-python"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --without-python \
                     --libdir=/usr/lib32"
        shelltools.export("CC", "%s -m32" % get.CC())

    autotools.configure(options)

def build():
    #needed by mozilla patch, swig must be run again
    shelltools.cd("python")
    shelltools.system("./swig_lcms")
    shelltools.cd("..")

    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s \
                          BINDIR=%s/usr/bin \
                          includedir=/usr/include' % (get.installDIR(), get.installDIR()))

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")

    pisitools.insinto("/usr/share/lcms/profiles", "testbed/*.icm")

    pisitools.dodoc("AUTHORS", "README*", "NEWS", "doc/*")
