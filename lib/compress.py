# -*- coding: utf-8 -*-
"""
functions for image stack (un-)compression
"""
import bz2


def bz2_compress_stack(stack_name):
    """" Takes stack file and compresses it into bz2 archive with the same name + '.bz2' extension
    Arguments
    ---------
    stack_name: str
        Full path name of the source stack.
    Returns
    -------
    none
    """
    with open(stack_name, 'rb') as f:
        data = f.read()
    with bz2.BZ2File(stack_name + '.bz2', "wb") as fout:
        fout.write(data)
    return


def bz2_uncompress_stack(archive_name):
    """" Takes .bz2 archive and unpacks it into file with the same name, minus '.bz2' extension
    Arguments
    ---------
    archive_name: str
        Full path name of the source archive.
    Returns
    -------
    none
    """
    with bz2.BZ2File(archive_name, 'rb') as fin:
        data = fin.read()
    stack_filename = archive_name[:-4]  # chop the '.bz2' extension for raw file name
    with open(stack_filename, 'wb') as f:
        f.write(data)
    return
