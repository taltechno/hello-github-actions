import pytest
from hello import greet


def test_greeting() -> None:
    assert greet("Testname") == "Hello, Testname!"
