#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-theora \
                         --enable-speex")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/bin")
