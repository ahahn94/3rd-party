#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "241.18034.69"

def install():
    pisitools.insinto("/opt/phpstorm", "PhpStorm-%s/*" % Build)
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
