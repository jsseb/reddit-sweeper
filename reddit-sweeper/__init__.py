#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from .sweeper import Sweeper, DownloadError
from docopt import docopt

__doc__ = """Usage: reddit_sweeper.py [-vqrh] [FILE]
          reddit_sweeper.py (--left | --right) CORRECTION FILE
Process FILE and optionally apply correction to either left-hand side or
right-hand side.
Arguments:
  CONFIG        optional config file
  CORRECTION    correction angle, needs FILE, --left or --right to be present
Options:
  -h --help             Print this help text and exit.
  --version             Print program version and ext.
  -i --ignore-errors    Continue on download errors, skipping non available files.
  -v --verbose          Verbose mode
  -c --config           Load custom config file.

"""
__license__ = 'MIT License'
__version__ = '0.1'


def main(argv=None):
    try:
        args = docopt(__doc__)
        with Sweeper(args) as swr:
            retcode = swr.download(args['url'])
        sys.exit(retcode)
    except DownloadError:
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by the user.')

__all__ = ['Sweeper']