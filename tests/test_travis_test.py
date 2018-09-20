#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `travis_test` package."""

import sys
sys.path.append('../')

import pytest
import unittest

from click.testing import CliRunner

from travis_test import travis_test
from travis_test import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'travis_test.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


class test_ckhr(unittest.TestCase):
    def test_calc_add(self):
        res = travis_test.calc_add(2,3)
        assert res == 5
        assert travis_test.c == 9


if __name__ == '__main__':
    unittest.main()

