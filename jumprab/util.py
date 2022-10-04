# -*- coding: utf-8 -*-

import shutil
import os


def file_clone(src, dst, **kwargs):
    """Just link shutil.copy2() but also clone the user id and group id either"""

    shutil.copy2(src, dst, **kwargs)
    stat = os.stat(src)
    shutil.chown(dst, stat.st_uid, stat.st_gid)
