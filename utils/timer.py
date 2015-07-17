#!/usr/bin/env python
# coding=utf-8
""" Time execution of code.

Example:

with Timer(verbose=True) as t:
    your_code_here
"""
import time

__author__ = 'julenka'

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs

