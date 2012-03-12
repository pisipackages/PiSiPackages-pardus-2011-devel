#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pygtkglext-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-gtkglext-test")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING","README")
