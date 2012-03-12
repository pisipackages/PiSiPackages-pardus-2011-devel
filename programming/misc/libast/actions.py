#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--disable-static \
                         --with-x \
                         --with-imlib \
                         --enable-mmx \
                         --with-regexp \
                         --enable-pcre")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("DESIGN", "README", "ChangeLog")

