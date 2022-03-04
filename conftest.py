import pytest
import requests


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


@pytest.fixture(autouse=True)
def disable_network_call(monkeypatch):  # This will disable sending a get request from any test case
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
