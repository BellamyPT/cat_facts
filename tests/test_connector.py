from unittest import mock

import pytest

from cat_facts.connector import Connector


@pytest.fixture
def mock_connector():
    return Connector()

def test_connector_init(mock_connector):
    assert mock_connector.api_url == "https://catfact.ninja/fact"

@mock.patch("cat_facts.connector.requests.get", autospec=True)
@mock.patch("cat_facts.connector.sleep", autospec=True)
def test_connector_extract_info(mock_sleep, mock_get, mock_connector):
    mock_connector.extract_info()
    mock_sleep.assert_called_once()
    mock_get.assert_called_once()
