#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rooki` package."""

from .common import ROOK_URL


def test_rooki_settings(rooki):
    assert rooki.url == ROOK_URL
    assert rooki.mode == 'sync'
    assert rooki.verify is False


def test_rooki_subset(rooki):
    resp = rooki.subset(
        collection='c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest')
    assert resp.ok is True
    assert resp.num_files == 1
    assert len(resp.download_urls()) == 1
