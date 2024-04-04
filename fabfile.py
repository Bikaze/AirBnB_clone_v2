#!/usr/bin/python3
"""
This Fabric script generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the do_pack task.
"""
import os
from datetime import datetime
from os.path import isdir, exists
from fabric import task

@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if the archive has been correctly generated,
    otherwise returns None.
    """
    try:
        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create the versions folder if it doesn't exist
        if not isdir("versions"):
            c.run("mkdir versions")

        # Generate the archive name
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)

        # Create the archive
        print("Packing web_static to {}".format(archive_path))
        c.run("tar -cvzf {} web_static".format(archive_path))

        # Check if the archive was created successfully
        if exists(archive_path):
            print("web_static packed: {} -> {}Bytes".format(archive_path, str(os.path.getsize(archive_path))))
            return archive_path
        else:
            return None

    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
