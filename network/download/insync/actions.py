#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import pisitools, shelltools, get

NoStrip = ["/etc", "/usr"]
KeepSpecial = ["python"]

def setup():
    shelltools.system("ar xf insync_{}-*_amd64.deb".format(get.srcVERSION() ) )
    shelltools.system("tar xvf data.tar.gz")
    shelltools.system("mv usr/share/applications/insync.desktop usr/share/applications/insync.py.desktop")
    shelltools.system("rm usr/bin/insync")
    #Remove empty folders that cause conflicts with hicolor-icon-theme
    shelltools.system("rmdir usr/share/icons/hicolor/{16x16,32x32}/emblems")

    # enable status indicators the in nautilus file manager; requires the package
    #    nautilus-python to be installed (should be installed automatically as
    #    a dependency from pspec.xml)
    shelltools.system("ar xf insync-nautilus*_all.deb")
    shelltools.system("tar xvf data.tar.gz")

    # a similar package exists for the caja file manager but requires python-caja
    #    to be packaged for Solus first

def install():
    pisitools.insinto("/", "usr")
