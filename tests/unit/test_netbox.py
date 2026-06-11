import pytest
from unittest.mock import Mock
from netauto.integrations.netbox import NetBoxClient


def test_get_device_by_name_found(mocker):
    """Returns the device when NetBox has it."""
    mock_api = Mock()
    mock_device = Mock()
    mock_device.name = "test-device"
    mock_api.dcim.devices.get.return_value = mock_device
    mocker.patch("netauto.integrations.netbox.pynetbox.Api", return_value=mock_api)

    client = NetBoxClient(Netbox_url="http://fake", Netbox_token="fake-token")
    result = client.get_device_by_name("test-device")

    assert result is not None
    assert result.name == "test-device"


def test_get_device_by_name_not_found(mocker):
    """Returns None when the device does not exist."""
    mock_api = Mock()
    mock_api.dcim.devices.get.return_value = None
    mocker.patch("netauto.integrations.netbox.pynetbox.Api", return_value=mock_api)

    client = NetBoxClient(Netbox_url="http://fake", Netbox_token="fake-token")
    result = client.get_device_by_name("ghost-device")

    assert result is None


def test_get_interfaces_found(mocker):
    """Returns a list of interface dicts when the device has interfaces."""
    mock_api = Mock()
    mock_api.dcim.devices.get.return_value = Mock()  # device exists (truthy)
    mock_api.dcim.interfaces.filter.return_value = [
        {"name": "GigabitEthernet0/1"},
        {"name": "GigabitEthernet0/2"},
    ]
    mocker.patch("netauto.integrations.netbox.pynetbox.Api", return_value=mock_api)

    client = NetBoxClient(Netbox_url="http://fake", Netbox_token="fake-token")
    result = client.get_interfaces("test-device")

    assert isinstance(result, list)
    assert len(result) == 2


def test_get_interfaces_device_missing(mocker):
    """Returns None when the device itself does not exist."""
    mock_api = Mock()
    mock_api.dcim.devices.get.return_value = None
    mocker.patch("netauto.integrations.netbox.pynetbox.Api", return_value=mock_api)

    client = NetBoxClient(Netbox_url="http://fake", Netbox_token="fake-token")
    result = client.get_interfaces("ghost-device")

    assert result is None


def test_get_device_by_name_handles_exception(mocker):
    """Catches NetBox errors and returns None instead of crashing."""
    mock_api = Mock()
    mock_api.dcim.devices.get.side_effect = Exception("connection boom")
    mocker.patch("netauto.integrations.netbox.pynetbox.Api", return_value=mock_api)

    client = NetBoxClient(Netbox_url="http://fake", Netbox_token="fake-token")
    result = client.get_device_by_name("test-device")

    assert result is None