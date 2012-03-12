#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.copy("tools/gnome-doc-utils.m4", "m4/")
    autotools.autoreconf("-fiv")
    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS")
