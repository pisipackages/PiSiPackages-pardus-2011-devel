#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pynifti-%s" % get.srcVERSION().split("_")[1]

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHOR", "COPYING", "Changelog", "PKG-INFO", "TODO")
    pisitools.doman("man/*")
