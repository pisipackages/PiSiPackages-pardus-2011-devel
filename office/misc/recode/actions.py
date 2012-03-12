# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("m4/libtool.m4")
    shelltools.unlink("acinclude.m4")
    autotools.autoreconf("-vif")

    autotools.configure("--enable-nls \
                         --without-included-gettext \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "BACKLOG", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
