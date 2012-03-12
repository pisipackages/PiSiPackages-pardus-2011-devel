#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="ps2eps"

def build():
    shelltools.cd("src/C/")
    shelltools.system("cc -o bbox bbox.c")

def install():
    pisitools.dobin("src/C/bbox")
    pisitools.dobin("bin/ps2eps")
    pisitools.dohtml("doc/html/*")
    pisitools.doman("doc/man/man1/bbox.1", "doc/man/man1/ps2eps.1")

    pisitools.dodoc("Changes.txt", "README.txt", "doc/pdf/*")
