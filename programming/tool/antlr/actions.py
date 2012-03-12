# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    shelltools.system('find . -name "*.jar" -exec rm -f {} \;')

    shelltools.system("ant jar")

    shelltools.copy("work/lib/antlr.jar", ".")
    shelltools.export("CLASSPATH", ".")

    autotools.configure("--enable-java \
                         --enable-python \
                         --disable-mono \
                         --enable-cxx \
                         --disable-examples \
                         --enable-verbose")

def build():
    autotools.make('CXXFLAGS="%s -fPIC"' % get.CXXFLAGS())
    shelltools.unlink("antlr.jar")

def install():
    pisitools.insinto("/usr/share/java","work/lib/antlr.jar")

    pisitools.dosed("scripts/run-antlr", "^ANTLR_JAR=.*", 'ANTLR_JAR="/usr/share/java/antlr.jar"')
    pisitools.dobin("scripts/run-antlr")
    pisitools.domove("/usr/bin/run-antlr", "/usr/bin", "antlr")

    pisitools.insinto("/usr/include/antlr", "lib/cpp/antlr/*.hpp")
    pisitools.dolib("lib/cpp/src/*.a")
    pisitools.dobin("scripts/antlr-config")

    pisitools.insinto("/usr/lib/%s/site-packages" % get.curPYTHON(), "lib/python/antlr")

    pisitools.dodoc("CHANGES.txt","README.txt", "LICENSE*")

