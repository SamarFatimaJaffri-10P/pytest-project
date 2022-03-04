import pytest
from main import format_data_for_excel
from main import format_data_for_display


def test_format_data_for_display_(example_people_data):
    assert format_data_for_display(example_people_data) == [
        'Talha Ghaffar: Staff Software Engineer',
        'Samar Jaffri: Associate Software Engineer'
    ]


def test_format_data_for_excel_(example_people_data):
    assert format_data_for_excel(example_people_data) == '''given,family,title
Talha,Ghaffar,Staff Software Engineer
Samar,Jaffri,Associate Software Engineer'''
