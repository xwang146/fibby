#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from fibby.skeleton import fib

__author__ = "Xinyuan Wang"
__copyright__ = "Xinyuan Wang"
__license__ = "mit"


def test_main():
    assert main(["tests/test2.sl"])=='7'
