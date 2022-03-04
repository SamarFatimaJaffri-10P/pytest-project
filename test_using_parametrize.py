import pytest
from main import is_palindrome


@pytest.mark.parametrize('palindrome', [
    '',
    'a',
    'Bob',
    'Never odd or even',
    "Let's test this one"
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)


@pytest.mark.parametrize('non_palindrome', [
    'abc',
    'cap'
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)


@pytest.mark.parametrize('maybe_palindrome, expected_results', [
    ('', True),
    ('a', True),
    ('Bob', True),
    ('Never odd or even', True),
    ("Let's test this one", True),
    ('abc', False),
    ('cap', False)
])
def test_is_palindrome_(maybe_palindrome, expected_results):
    assert is_palindrome(maybe_palindrome) == expected_results
