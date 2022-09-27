# -*- coding: utf-8 -*-

"""Top-level package for jumprab."""

__author__ = """Hong-She Liang"""
__email__ = "sorn@taorules.com"
__version__ = "0.0.1"

from .flutterjumper import FlutterJumper
from .pipjumper import PipJumper
from .flatpakjumper import FlatpakJumper
from .dockerjumper import DockerJumper

jumpers = {
    PipJumper,
    FlatpakJumper,
    FlutterJumper,
    DockerJumper,
}

def get_jumper_map():
    """Get jumper map for it's TAG"""
    # type: () -> Dict[str]
    jumper_map = dict()

    for it in jumpers:
        jumper_map[it.TAG] = it

    return jumper_map
