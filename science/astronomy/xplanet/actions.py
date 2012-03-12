#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-xscreensaver \
                         --with-freetype \
                         --with-pango \
                         --with-cspice \
                         --with-gif \
                         --with-jpeg \
                         --with-png \
                         --with-pnm \
                         --with-tiff")


def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "TODO")
