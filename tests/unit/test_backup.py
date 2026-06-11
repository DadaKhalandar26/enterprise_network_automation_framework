import pytest
from netauto.services.backup import BackUp


def test_device_back_up_by_name(mocker):
    # 1. Patch everything FIRST
    mocker.patch("netauto.services.backup.DeviceConnectionHandler")
    mocker.patch("netauto.services.backup.os.path.exists", return_value=True)
    mocker.patch("netauto.services.backup.os.makedirs")
    mocker.patch("builtins.open", mocker.mock_open())

    # 2. THEN create BackUp (now it gets the fake handler)
    test_BackUp = BackUp(
        Netbox_url="https://fake-url",
        Netbox_token="fake-token",
        user_name="fake-user",
        Password="fake-Password",
        enbable_password=None,
    )

    # 3. Tell the fake handler what to return
    test_BackUp.Connect_to.execute_command.return_value = "fake config output"

    # 4. Call the function and check
    result = test_BackUp.device_back_up_by_name(device="test-device")

    assert result is True
    
    
