#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-apr=/usr \
                         --includedir=/usr/include/apr-1 \
                         --with-ldap \
                         --without-gdbm \
                         --with-sqlite3 \
                         --with-pgsql \
                         --with-odbc=/usr/bin/odbc_config \
                         --with-mysql \
                         --without-freetds \
                         --with-berkeley-db \
                         --without-sqlite2")

def build():
    autotools.make("-j1")

def check():
    autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Not used
    pisitools.remove("/usr/lib/aprutil.exp")

    pisitools.dosed("%s/usr/bin/apu-1-config" % get.installDIR(), get.workDIR(), "")

    pisitools.dodoc("CHANGES", "NOTICE")
