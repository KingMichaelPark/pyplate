#!/usr/bin/env python

"""Tests for `python_boilerplate` package."""

import pytest
from click.testing import CliRunner

from python_boilerplate import cli, python_boilerplate


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    assert python_boilerplate  # Remove this (Just to get tox to pass)
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """
    Sample pytest test function with the pytest fixture as an argument.

    :arg response: The response fixture.
    :type response: None

    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "python_boilerplate.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
