#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("DEFS", "NO_ASM")
    autotools.configure("--exec-prefix=/")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add missing gzcat
    pisitools.dosym("zcat", "/bin/gzcat")

    pisitools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO")
