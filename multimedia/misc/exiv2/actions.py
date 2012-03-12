#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "COPYING", "doc/ChangeLog")
