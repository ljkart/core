"""Nuke initialisation file

This is where Nuke is setup with everything related to
avalon-core. For studio or shot-specific setup,
try and not use this file, but rather an external file
that is then added to NUKE_PATH alongside this one.

Think of how others would use avalon-core on another
machine not on your network.

"""


def setup():
    print("pipeline: Setting up..")

    from pyblish import api
    api.register_gui("pyblish_lite")

    from avalon import api, nuke
    api.install(nuke)

    print("pipeline: Finished!")


setup()
