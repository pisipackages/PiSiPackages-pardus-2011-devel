#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.dodoc("README", "MANIFEST", "LICENSE" , "CHANGES", "COPYING")
