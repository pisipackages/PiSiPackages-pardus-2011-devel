#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
WorkPath="%s/%s"  % (get.workDIR(), get.srcDIR())

def setup():
    shelltools.touch("GNUstep.conf")
    shelltools.echo("GNUstep.conf", "GNUSTEP_USER_DIR=%s" % get.workDIR())
    shelltools.echo("GNUstep.conf", "GNUSTEP_USER_DEFAULTS_DIR=%s/Defaults" % get.workDIR())
 
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-ffcall \
                        --enable-gnutls \
                        --enable-tls \
                        --enable-zeroconf \
                        --with-default-config=%s/GNUstep.conf" % WorkPath)

def build():
    autotools.make()

    shelltools.export("LD_LIBRARY_PATH", "%s/%s/Source/obj:${LD_LIBRARY_PATH}" % (get.workDIR(), get.srcDIR()))
    autotools.make("-C Documentation \
                    GNUSTEP_CONFIG_FILE=%s/GNUstep.conf" % WorkPath)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C Documentation" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS")
