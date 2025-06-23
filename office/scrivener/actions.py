#!/usr/bin/env python3

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf scrivener-%s-amd64.deb" % Version)
    shelltools.system("tar xf data.tar.gz")
    shelltools.system("asciify usr")
    shelltools.system("mkdir usr/share/icons/hicolor")
    pisitools.move("usr/share/icons/*x*", "usr/share/icons/hicolor/")
    shelltools.system("rm usr/share/scrivener/bin/scrivener.sh")

def install():
    pisitools.insinto("/", "usr")
    pisitools.removeDir("/usr/share/doc")
    pisitools.removeDir("/usr/share/scrivener/lib/pkgconfig")
