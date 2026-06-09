import netmiko, scrapli, ipaddress
from ..integrations.netbox import NetBoxClient
from ..utils import logger
from ..config.settings import Env_Setting

log = logger.get_logger("DeviceConnectionHandler_logger")

NETMIKO_SUPPORTED_PLATFORMS = ["Cisco IOS", "Cisco IOS-XE", "Cisco NX-OS", "Arista EOS", "Juniper Junos"]
NETMIKO_PlATFORM_MAPPING = {"Cisco IOS": "cisco_ios",
                            "Cisco IOS-XE": "cisco_xe",
                            "Cisco NX-OS": "cisco_nxos",
                            "Arista EOS": "arista_eos",
                            "Juniper Junos": "juniper_junos",
                            }
# SCRAPLI_SUPPORTED_PLATFORMS = ["Cisco IOS", "Cisco IOS-XE", "Cisco NX-OS", "Arista EOS"]

class DeviceConnectionHandler:
    """Handle NetBox device resolution and Netmiko command execution."""

    def __init__(self, Netbox_url, Netbox_token, user_name, Password, enbable_password: str | None):
        """Initialize the handler with NetBox credentials and device login details."""
        log.info("Initializing DeviceConnectionHandler with NetBox and device credentials.")
        Setting = Env_Setting()
        
        self.Netbox_url = Netbox_url
        self.Netbox_token = Netbox_token
        self.user_name = user_name
        self.password = Password
        self.enable_password = enbable_password
        self.NetBox = NetBoxClient(Netbox_url=self.Netbox_url, Netbox_token=self.Netbox_token)
        self.Netmiko_Handler = netmiko.ConnectHandler

    def execute_command(self, device_name, command: str):
        """Lookup a device in NetBox and execute a CLI command on it via Netmiko."""
        log.info(f"Beginning execute_command for device '{device_name}'.")
        try:
            device = self.NetBox.get_device_by_name(device_name=device_name)
            if device:
                device_details = {
                    'host name': device.name,
                    'platform': device.platform.name if device.platform else None,
                    'role': device.role.name if device.role else None,
                    'site': device.site.name if device.site else None,
                    'Managment IP': str(ipaddress.ip_interface(device.primary_ip).ip) if device.primary_ip else None
                }
                log.info(
                    f"Device '{device_name}' resolved from NetBox with platform={device_details.get('platform')}, "
                    f"site={device_details.get('site')}.")
                if device_details.get("platform") in NETMIKO_SUPPORTED_PLATFORMS:
                    netmiko_device_type = NETMIKO_PlATFORM_MAPPING[device_details.get("platform")]
                    device_connection_data = {
                        "device_type": netmiko_device_type,
                        "host": device_details.get("Managment IP"),
                        "username": self.user_name,
                        "password": self.password,
                        "secret": self.enable_password
                    }
                    log.info(
                        f"Connecting to '{device_details.get('host name')}' at {device_details.get('Managment IP')} "
                        f"using Netmiko device_type='{netmiko_device_type}'.")
                    Netmiko_connector = self.Netmiko_Handler(**device_connection_data)
                    output = Netmiko_connector.send_command(command)
                    Netmiko_connector.disconnect()
                    if output:
                        log.info("Command executed successfully and output was returned.")
                        return output
                    log.warning("Command executed successfully but returned no output.")
                    return None
            else:
                log.error(f"Device '{device_name}' could not be found in NetBox.")
                return None
        except ValueError as e:
            log.error(f"ValueError while executing command on '{device_name}': {e}")
        except AttributeError as a:
            log.error(f"AttributeError while executing command on '{device_name}': {a}")
        except Exception as e:
            log.error(f"Unexpected error while executing command on '{device_name}': {e}")
        return None
    
if __name__ == "__main__":
    Setting = Env_Setting()
    
    connect_to = DeviceConnectionHandler(Netbox_url=Setting.NETBOX_DEV_URL, Netbox_token=Setting.NETBOX_DEV_TOKEN_RW.get_secret_value(), user_name=Setting.DEVICE_USERNAME, Password=Setting.DEVICE_PASSWORD.get_secret_value(), enbable_password=Setting.DEVICE_ENABLE_PASSWORD.get_secret_value())
    
    output = connect_to.execute_command(device_name="IN-HYD-LAB1-ACC-01",command="Show IP int Br")
    print(output)
