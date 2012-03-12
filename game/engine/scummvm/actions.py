#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --enable-verbose-build \
                            --backend=sdl \
                            --enable-alsa \
                            --enable-flac \
                            --enable-mad \
                            --with-nasm-prefix=/usr/bin/nasm \
                            --enable-vorbis \
                            --enable-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/he/*.html")
    pisitools.dodoc("AUTHORS", "COPYING", "COPYRIGHT", "NEWS", "README", "TODO", "doc/he/*.txt")
