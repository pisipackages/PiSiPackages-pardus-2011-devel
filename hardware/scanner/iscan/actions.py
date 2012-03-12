#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

iscan_data = "iscan-data-1.8.1"

def setup():
    # Setup iscan-data
    shelltools.cd(iscan_data)
    autotools.configure()
    shelltools.cd("..")

    shelltools.unlink("m4/libtool.m4")

    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --enable-frontend \
                         --enable-gimp=no \
                         --enable-jpeg \
                         --enable-tiff \
                         --enable-png \
                         --enable-dependency-reduction \
                         --disable-rpath")

def build():
    autotools.make("-C %s" % iscan_data)
    autotools.make()
    autotools.make("-C po update-po")

def install():
    autotools.install()
    autotools.install("-C %s" % iscan_data)

    # Remove unused stuff from iscan-data
    pisitools.remove("/usr/share/iscan-data/sled10*")
    pisitools.remove("/usr/share/iscan-data/fdi.xsl")

    # Install sane backend configuration file
    pisitools.insinto("/etc/sane.d", "backend/epkowa.conf")

    # Install documentation
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "%s/SUPPORTED-DEVICES" % iscan_data)

    # Needed for iscan-registry
    pisitools.dodir("/var/lib/iscan")
