#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr")

def build():
    shelltools.system("lrelease src/lang/qbittorrent_tr.ts")
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "Changelog", "COPYING", "NEWS", "README", "TODO")
