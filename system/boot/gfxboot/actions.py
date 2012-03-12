#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("Makefile", "^CC.*", "CC = %s" % get.CC())
    pisitools.dosed("doc/Makefile", "xmlto", "xmlto --skip-validation")

def build():
    shelltools.export("HOME", get.workDIR())
    autotools.make("X11LIBS=/usr/lib")
    autotools.make("doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.make('DESTDIR="%s" installsrc' % get.installDIR())

    pisitools.dodoc("doc/*.txt", "doc/*.html")
