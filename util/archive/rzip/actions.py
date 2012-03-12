#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make('CC="%s" \
                    CFLAGS="%s -O3 %s"' % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dobin("rzip")

    pisitools.doman("rzip.1")
    pisitools.dodoc("COPYING")
