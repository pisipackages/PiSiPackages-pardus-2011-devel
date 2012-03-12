#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("various/rline/src/rline.c", "cgdb_malloc", "malloc")
    autotools.configure()

def build():
    autotools.make()
    autotools.make("html")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS", "TODO")
    pisitools.dohtml("doc/cgdb.html/*")

