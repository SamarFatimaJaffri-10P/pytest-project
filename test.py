import pytest


def test_always_passes():
    assert True


def test_always_fails():
    assert False


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


def format_data_for_display(people):
    formatted_data = []
    for person in people:
        full_name = f"{person['given_name']} {person['family_name']}"
        formatted = f"{full_name}: {person['title']}"
        formatted_data.append(formatted)
    return formatted_data


def test_format_data_for_display():
    people = [
        {
            'given_name': 'Talha',
            'family_name': 'Ghaffar',
            'title': 'Staff Software Engineer'
        },
        {
            'given_name': 'Samar',
            'family_name': 'Jaffri',
            'title': 'Associate Software Engineer'
        },
    ]

    assert format_data_for_display(people) == [
        'Talha Ghaffar: Staff Software Engineer',
        'Samar Jaffri: Associate Software Engineer',
    ]


def format_data_for_excel(people):
    formatted_data = 'given,family,title'
    for person in people:
        formatted_data += f"""
{person['given_name']},{person['family_name']},{person['title']}"""

    return formatted_data


def test_format_data_for_excel():
    people = [
        {
            'given_name': 'Talha',
            'family_name': 'Ghaffar',
            'title': 'Staff Software Engineer'
        },
        {
            'given_name': 'Samar',
            'family_name': 'Jaffri',
            'title': 'Associate Software Engineer'
        },
    ]

    assert format_data_for_excel(people) == '''given,family,title
Talha,Ghaffar,Staff Software Engineer
Samar,Jaffri,Associate Software Engineer'''
