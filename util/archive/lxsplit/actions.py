#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile","^CFLAGS.*","CFLAGS = %s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("lxsplit")

    pisitools.dodoc("README", "ChangeLog")
