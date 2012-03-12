#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007,2008,2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--without-included-libmad \
                         --without-included-tre \
                         --without-included-argv")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "CHANGES", "README", "parse_rules.txt")
