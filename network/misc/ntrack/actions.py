#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.makedirs("m4")
    autotools.autoreconf("-vfi")
    autotools.configure("   --disable-static \
                            --with-glib2 \
                            --with-gobject \
                            --with-pygobject \
                            --with-qt4")

def build():
    autotools.make()

def install():
    autotools.install()

