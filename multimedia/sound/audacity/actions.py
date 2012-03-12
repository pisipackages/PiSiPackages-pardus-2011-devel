#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "audacity-src-%s-beta" % get.srcVERSION()

def setup():
    shelltools.cd("lib-src/portmixer")
    autotools.autoreconf()
    shelltools.cd("../..")

    autotools.aclocal("-I m4")
    autotools.autoconf()
    shelltools.export("LIBS", "-lavcodec")
    autotools.configure("--enable-unicode \
                         --enable-nyquist \
                         --enable-ladspa \
                         --with-lib-preference='system local' \
                         --with-libsndfile=system \
                         --with-expat=system \
                         --with-libsamplerate \
                         --with-libvorbis \
                         --with-libmad \
                         --with-libflac \
                         --with-libid3tag \
                         --with-sbsms \
                         --with-soundtouch \
                         --with-libvamp \
                         --with-libtwolame \
                         --with-ffmpeg \
                         --with-midi \
                         --with-taglib \
                         --with-portmixer")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/audacity/help/manual")
