#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob
import os.path

shelltools.export("LC_ALL", "C")

def setup():
    autotools.autoreconf("-fi")

    # Static libs should be enabled for mono compiler
    autotools.configure("--enable-parallel-mark \
                         --with-profile4=yes \
                         --with-tls=pthread \
                         --with-jit=yes \
                         --with-sgen=no \
                         --with-libgdiplus=installed \
                         --prefix=/usr \
                         --sysconfdir=/etc \
                         --with-monotouch=no ")

def build():
    shelltools.export("MONO_SHARED_DIR", get.curDIR())
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # These work on Windows only
    for i in glob.glob("%s/usr/lib/mono/*/Mono.Security.Win32*" % get.installDIR()):
        x = i.split(get.installDIR())[-1]
        if os.path.isdir(x):
            pisitools.removeDir(x)
            continue

        pisitools.remove(x)

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "NEWS", "README")
