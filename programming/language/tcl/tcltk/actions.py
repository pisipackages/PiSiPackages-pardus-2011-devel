#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="tk%s" % get.srcVERSION()

def setup():
    shelltools.cd("unix")
    autotools.autoconf()
    autotools.configure("--with-encoding=utf-8 \
                         --enable-threads \
                         --enable-man-compression=gzip \
                         --enable-man-symlinks \
                         --enable-64bit \
                         --with-x \
                         --enable-xft")

def build():
    autotools.make("-C unix")

def install():
    shelltools.system("make -C unix DESTDIR=%s install" % get.installDIR())

    # Collect private headers, 3rd party apps like Tile depends on this
    pisitools.dodir("/usr/include/tk-private/generic")
    pisitools.dodir("/usr/include/tk-private/unix")
    shelltools.copy("unix/*.h", "%s/usr/include/tk-private/unix" % get.installDIR())
    shelltools.copy("generic/*.h", "%s/usr/include/tk-private/generic" % get.installDIR())

    # Remove duplicated headers
    pisitools.remove("/usr/include/tk-private/generic/tk.h")
    pisitools.remove("/usr/include/tk-private/generic/tkDecls.h")
    pisitools.remove("/usr/include/tk-private/generic/tkPlatDecls.h")

    # Remove tmp path from tclConfig.sh
    pisitools.dosed("%s/usr/lib/tkConfig.sh" % get.installDIR(), "%s/unix" % get.curDIR(), "/usr/lib/")
    pisitools.dosed("%s/usr/lib/tkConfig.sh" % get.installDIR(), get.curDIR(), "/usr/include/tk-private")

    pisitools.dosym("/usr/bin/wish8.5", "/usr/bin/wish")

    pisitools.dodoc("ChangeLog", "changes", "license.terms", "README")
