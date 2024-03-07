#!/usr/bin/python3
"""This module will deploy the web static folder to the web servers"""
from fabric.api import *
from datetime import datetime
from os import path


# setting up the user, hosts and private key
env.hosts = ['54.157.130.35', '3.90.70.134']
env.user = 'ubuntu'
env.path_to_key = '/root/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes the web static folder to the web servers"""
    try:
        # cheching if the file at the archive_path exists
        if not path.exists(archive_path):
            return False

        # uploading the files to the webservers
        put(archive_path, '/tmp/')

        # creating the new directory to uncompress the files to
        no_exe = archive_path[-18:-4]  # removing the extensions
        run(f'sudo mkdir -p /data/web_static/releases/web_static_{no_exe}/')
        
        # uncompressing the archive to a folder
        run(f'tar -xzf /tmp/web_static_{no_exe}.tgz -C /data/web_static/releases/web_static_{no_exe}/')

        # deleting the archive from web server
        run(f'sudo rm /tmp/web_static_{no_exe}.tgz')
        run(f'sudo mv /data/web_static/releases/web_static_{no_exe}/web_static/* /data/web_static/releases/web_static_{no_exe}/')
        run(f'sudo rm -rf /data/web_static/releases/web_static_{no_exe}/web_static')

        # deleting the sym link
        run('sudo rm -rf /data/web_static/current')

        # create new sym link
        run(f'sudo ln -s /data/web_static/releases/web_static_{no_exe}/ /data/web_static/current')

    except Exception:
        return False

    return True
