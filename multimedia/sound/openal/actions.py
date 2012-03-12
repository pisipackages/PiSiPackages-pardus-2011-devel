#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "openal-soft-%s" % get.srcVERSION()

def setup():
    options = "-DALSA=1 \
               -DPULSEAUDIO=1 \
               -DOSS=1"

    if get.buildTYPE() == "emul32":
        options += " -DCMAKE_INSTALL_PREFIX=/emul32 \
                     -DLIB_SUFFIX=32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    cmaketools.configure(options)

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # is there any "libdir" prefix for cmake ?
    if get.buildTYPE() == "emul32":
        from distutils.dir_util import copy_tree
        copy_tree("%s/emul32/lib32/" % get.installDIR(), "%s/usr/lib32" % get.installDIR())
        pisitools.removeDir("/emul32")
        return

    pisitools.dodoc("COPYING", "alsoftrc.sample")
