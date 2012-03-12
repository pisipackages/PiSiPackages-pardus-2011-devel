#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "xf86-video-ati-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-dri")

def build():
    autotools.make()

def install():
    autotools.install()
