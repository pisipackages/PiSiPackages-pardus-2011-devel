#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #Remove MacOS plugin
    shelltools.unlinkDir("plugins/address_book")
    shelltools.unlinkDir("plugins/growl")
    #Remove Win stuff
    shelltools.unlink("plugins/music/MusicWin*")
    shelltools.unlinkDir("skins/default/winicons")

    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CREDITS", "GNUGPL", "HELP", "README", "TODO", "docs/*")
