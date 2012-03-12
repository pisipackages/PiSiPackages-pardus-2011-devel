#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s" % get.srcDIR().replace("0.", "0.STABLE")

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure('--enable-shared=yes \
                         --enable-static=no \
                         --disable-dependency-tracking \
                         --enable-arp-acl \
                         --enable-follow-x-forwarded-for \
                         --enable-xmalloc-statistics \
                         --enable-auth="basic,digest,negotiate,ntlm" \
                         --enable-basic-auth-helpers="LDAP,MSNT,NCSA,PAM,SMB,YP,getpwnam,multi-domain-NTLM,SASL,DB,POP3,squid_radius_auth" \
                         --enable-ntlm-auth-helpers="smb_lm,no_check,fakeauth" \
                         --enable-digest-auth-helpers="password,ldap,eDirectory" \
                         --enable-negotiate-auth-helpers="squid_kerb_auth" \
                         --enable-external-acl-helpers="ip_user,ldap_group,session,unix_group,wbinfo_group" \
                         --enable-cache-digests \
                         --enable-cachemgr-hostname="localhost" \
                         --enable-delay-pools \
                         --enable-epoll \
                         --enable-icap-client \
                         --enable-ident-lookups \
                         --with-large-files \
                         --enable-referer-log \
                         --enable-linux-netfilter \
                         --enable-removal-policies="heap,lru" \
                         --enable-snmp \
                         --enable-ssl \
                         --enable-storeio="aufs,diskd,ufs" \
                         --enable-useragent-log \
                         --enable-wccp \
                         --enable-wccpv2 \
                         --enable-esi \
                         --with-aio \
                         --with-default-user="squid" \
                         --with-filedescriptors=16384 \
                         --with-dl \
                         --with-openssl \
                         --with-pthreads \
                         --enable-mit=/usr \
                         --with-pidfile=/var/run/squid.pid \
                         --sysconfdir=/etc/squid \
                         --localstatedir=/var \
                         --libexecdir=/usr/lib/squid \
                         --datadir=/usr/share/squid \
                         --with-logdir=/var/log/squid')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/cache/squid")
    pisitools.dodir("/var/log/squid")

    pisitools.dosym("/usr/share/squid/errors/en", "/etc/squid/errors")

    pisitools.doman("helpers/basic_auth/LDAP/*.8")
    pisitools.dohtml("helpers/basic_auth/MSNT/README.html", "RELEASENOTES.html")
    pisitools.dodoc("helpers/basic_auth/SASL/squid_sasl_auth*")
    pisitools.dodoc("CONTRIBUTORS", "CREDITS", "ChangeLog", "QUICKSTART", "doc/*.txt", "helpers/ntlm_auth/no_check/README.no_check_ntlm_auth")
