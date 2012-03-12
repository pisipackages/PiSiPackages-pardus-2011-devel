#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # configure for sdl-client
    autotools.configure("--disable-dependency-tracking \
                         --enable-nls \
                         --with-readline \
                         --without-ggz-client \
                         --without-ggz-server \
                         --enable-shared \
                         --enable-static=no \
                         --enable-client=sdl")

def build():
    # compile sdl gui
    autotools.make()

    # backup sdl gui
    pisitools.dosed("client/freeciv.desktop", "freeciv-gtk2", "freeciv-sdl")
    shelltools.move("client/freeciv.desktop", "client/freeciv-sdl.desktop")
    shelltools.system("echo GenericName=Freeciv-SDL>>client/freeciv-sdl.desktop")

    # I need to configure twice to enable both sdl and gtk guis
    autotools.configure("--disable-dependency-tracking \
                         --enable-nls \
                         --with-readline \
                         --without-ggz-client \
                         --without-ggz-server \
                         --enable-shared \
                         --enable-static=no \
                         --enable-client=gtk-2.0")
    #compile gtk gui
    autotools.make()

def install():
    # gtk gui
    shelltools.system("echo GenericName=Freeciv-GTK>>client/freeciv.desktop")
    pisitools.insinto("/usr/share/applications", "client/freeciv.desktop", "freeciv-gtk2.desktop")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # sdl gui
    pisitools.dobin("client/.libs/freeciv-sdl")
    pisitools.insinto("/usr/share/applications", "client/freeciv-sdl.desktop", "freeciv-sdl.desktop")
    pisitools.insinto("/usr/share/freeciv/themes/gui-sdl", "data/themes/gui-sdl/human")

    # cleanup
    pisitools.remove("/usr/share/freeciv/themes/gui-sdl/human/Makefile*")
    pisitools.remove("/usr/share/applications/freeciv.desktop")

    # docs
    shelltools.system("./manual/civmanual")
    pisitools.dohtml("manual*.html")

    pisitools.dodoc("ChangeLog", "NEWS", "doc/BUGS", "doc/HOWTOPLAY", "doc/README*", "doc/TODO")
