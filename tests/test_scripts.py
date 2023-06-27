"""Test module."""
import pytest
from incolume.py.mailing.scripts import send_gmail

__author__ = "@britodfbr"  # pragma: no cover


@pytest.mark.xfail
def test_send_gmail():
    """"""
    send_gmail('dev@incolume.com.br')
    assert False
