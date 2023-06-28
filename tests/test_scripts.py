"""Test module."""
import pytest
import inspect
import pathlib
import logging
from incolume.py.mailing.scripts import send_mail

__author__ = "@britodfbr"  # pragma: no cover


@pytest.mark.xfail
def test_send_mail():
    """"""
    send_mail('dev@incolume.com.br')
    assert False


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (inspect, True),
        (pathlib, True),
        (pathlib.Path, False),
        (send_mail, False),
    ),
)
def test_ismodule(entrance, expected):
    """Verifica se é módulo."""
    assert inspect.ismodule(entrance) == expected


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (inspect, False),
        (pathlib, False),
        (pathlib.Path, False),
        (send_mail, True),
    ),
)
def test_isfunction(entrance, expected):
    """Verifica se é função."""
    assert inspect.isfunction(entrance) == expected


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (inspect, False),
        (pathlib, False),
        (pathlib.Path, True),
        (send_mail, False),
    ),
)
def test_isclass(entrance, expected):
    """Verifica se é classe."""
    assert inspect.isclass(entrance) == expected


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (inspect, False),
        (pathlib, False),
        (pathlib.Path, False),
        (send_mail, False),
    ),
)
def test_ismethod(entrance, expected):
    """Verifica se é método."""
    assert inspect.ismethod(entrance) == expected


@pytest.mark.parametrize(
    ('entrance', 'predicate', 'expected'),
    (
        pytest.param(inspect, inspect.isclass, True),
        pytest.param(pathlib, inspect.isclass, True),
        pytest.param(pathlib.Path, inspect.isclass, True),
        pytest.param(send_mail, inspect.isclass, True),
        pytest.param(inspect, inspect.ismodule, True),
        pytest.param(pathlib, inspect.ismodule, True, marks=pytest.mark.skip),
        pytest.param(pathlib.Path, inspect.ismodule, False),
        pytest.param(send_mail, inspect.ismodule, False),
        pytest.param(inspect, inspect.ismethod, False),
        pytest.param(pathlib, inspect.ismethod, False),
        pytest.param(pathlib.Path, inspect.ismethod, True),
        pytest.param(send_mail, inspect.ismethod, False),
        pytest.param(inspect, inspect.isfunction, True),
        pytest.param(pathlib, inspect.isfunction, True),
        pytest.param(pathlib.Path, inspect.isfunction, True),
        pytest.param(send_mail, inspect.isfunction, False),
    ),
)
def test_checkeble(entrance, predicate, expected):
    """Verifica se a entrada possui predicados específicos, como classes,
     modulos, metodos e funções."""
    result = inspect.getmembers(entrance, predicate)
    logging.debug(result)
    print(result)
    assert bool(result) == expected
