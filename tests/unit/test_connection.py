import pytest
from unittest.mock import Mock
from netauto.core.connection import DeviceConnectionHandler


def test_execute_command(mocker):
    mock_NetBox = Mock()
    mock_device = Mock()
    mock_device.name = "test-Device"
    mock_device.platform.name = "Cisco IOS"
    mock_device.role.name = "Core Switch"
    mock_device.site.name = "Test-Site"
    mock_device.primary_ip = "10.0.0.1/24"
    mock_NetBox.get_device_by_name.return_value = mock_device

    mocker.patch("netauto.core.connection.NetBoxClient", return_value=mock_NetBox)

    mock_Netmiko_Handler = Mock()
    mock_Netmiko_Handler.send_command.return_value = "fake config output"
    mocker.patch("netauto.core.connection.netmiko.ConnectHandler", return_value=mock_Netmiko_Handler)

    handler = DeviceConnectionHandler(
    Netbox_url="http://fake",
    Netbox_token="fake-token",
    user_name="testuser",
    Password="testpass",
    enbable_password=None
    )
    result = handler.execute_command(device_name="test-device", command="show run")

    assert result is not None
    assert result == "fake config output"