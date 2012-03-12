#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "doc/README.bin")

    pisitools.domove("/usr/share/sphinx2/doc/*", "/usr/share/doc/sphinx2/")
    pisitools.removeDir("/usr/share/sphinx2/doc")
