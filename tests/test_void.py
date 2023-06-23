"""Module test."""

import pytest

__author__ = 'mdias'


def test_void(capsys):
    """Test void."""

    print('oi')
    out, err = capsys.readouterr()
    assert out.strip() == 'oi'
    assert err == ''


@pytest.mark.parametrize(
    'entrance',
    (
        'oi',
        'hi',
        'python',
    ),
)
def test_none(capsys, entrance):
    """Test none."""
    print(entrance)
    out, err = capsys.readouterr()
    assert out.strip() == entrance
