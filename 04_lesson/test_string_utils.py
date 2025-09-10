import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",[
    ("katerina", "Katerina"),
    ("Katerina", "Katerina"),
    ("hello world", "Hello world")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",[
    ("123kat", "123kat"),
    ("  ", "  "),
    ("", "")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",[
    ("  katerina", "katerina"),
    (" skypro", "skypro"),
    ("     hello", "hello")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",[
    ("", ""),
    ("   ", ""),
    ("skypro", "skypro")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected",[
    ("Katerina", "K", True),
    ("skypro", "y", True),
    ("hello", "l", True)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected",[
    ("", "a", False),
    ("skypro", "u", False),
    ("hello", "H", False)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected",[
    ("Katerina", "erina", "Kat"),
    ("skypro", "p", "skyro"),
    ("hello", "he", "llo")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected",[
    ("", "a", ""),
    ("skypro", "u", "skypro"),
    ("hello", " ", "hello")
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
