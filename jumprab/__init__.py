# -*- coding: utf-8 -*-

"""Top-level package for jumprab."""

__author__ = """Hong-She Liang"""
__email__ = "sorn@taorules.com"
__version__ = "0.0.1"

from .flutterjumper import FlutterJumper
from .pipjumper import PipJumper
from .flatpakjumper import FlatpakJumper

jumpers = {
    PipJumper.TAG: PipJumper,
    FlatpakJumper.TAG: FlatpakJumper,
    FlutterJumper.TAG: FlutterJumper,
}
