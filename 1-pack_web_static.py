#!/usr/bin/python3
"""file for function"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """creates .tgz file from contents of folder """
    try:
        date = datetime.now().srtftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        name = "web_static_{}.tgz".format(date)
        local("tar -cvzf versions/{}".format(name))
        return name
    except:
        return None
