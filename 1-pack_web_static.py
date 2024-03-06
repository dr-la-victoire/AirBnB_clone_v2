#!/usr/bin/python3
"""This module compresses the web static files into a .tgz archive"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """This function compreses the web_static file into the tgz archive"""
    # name the directory to archive
    name = "web_static"

    # give the archive file a new name
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    new_name = f"web_static_{time}.tgz"

    # archive it
    try:
        local(f"tar cvzf {new_name} {name}")

        # move it to the new directory located
        local("mkdir -p versions")
        local(f"mv {new_name} versions")

        return f"versions/{new_name}"
    except Exception as e:
        return None
