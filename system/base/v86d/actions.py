# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--without-klibc \
                            --with-x86emu")

def build():
    autotools.make("all testvbe")

def install():
    autotools.rawInstall("DESTDIR=%s install_testvbe" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
