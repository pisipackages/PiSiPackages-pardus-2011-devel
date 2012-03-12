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
    shelltools.export("CFLAGS", "%s -fsigned-char -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --with-gsm \
                         --with-dyn-default")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "README", "NEWS", "AUTHORS", "COPYING", "LICENSE*")
