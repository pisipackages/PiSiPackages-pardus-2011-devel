#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # Don't call gtk
    pisitools.dosed("data/icons/Makefile.in", "^install-data-local: .*$", "install-data-local: install-icons")
    autotools.configure("--disable-doc")

def build():
    autotools.make()

def install():
    autotools.install()
