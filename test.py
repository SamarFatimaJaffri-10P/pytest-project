import pytest
from main import format_data_for_excel
from main import format_data_for_display


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
