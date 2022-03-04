import pytest


@pytest.fixture
def example_people_data():
    return [
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
