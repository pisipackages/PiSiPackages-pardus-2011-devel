#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "zniper"

def build():
    autotools.make('-j1 linux_x86 \
                    CC="%s" \
                    CFLAGS="%s"' % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dobin("zniper")
    pisitools.dodoc("README")
    pisitools.doman("zniper.1")
