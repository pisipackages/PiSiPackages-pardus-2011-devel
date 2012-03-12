#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.configure("--disable-static \
                         --enable-pcre \
                         --enable-xml2 \
                         --with-raptor=system \
                         --with-regex-library=pcre \
                         --disable-gtk-doc \
                         --with-html-dir=%s" % docdir)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("%s/html" % docdir, "%s/%s/rasqal/*" % (get.installDIR(), docdir))
    pisitools.removeDir("%s/rasqal" % docdir)
    pisitools.dohtml("*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING*", "NEWS", "README")
