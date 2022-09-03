# -*- coding: utf-8 -*-

"""Top-level package for jumprab."""

__author__ = """Hong-She Liang"""
__email__ = "sorn@taorules.com"
__version__ = "0.0.1"

from .pipjumper import PipJumper

jumpers = {
    PipJumper.TAG: PipJumper,
}
