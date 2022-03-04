import pytest


@pytest.mark.run_it
def test_always_passes():
    assert True


def test_always_fails():
    assert False


@pytest.mark.run_it
def test_uppercase():
    assert 'uppercase letters'.upper() == 'UPPERCASE LETTERS'


def test_reverse_list():
    assert list(reversed([5, 4, 3, 2, 1])) == [1, 2, 3, 4, 5]


def test_prime():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }
