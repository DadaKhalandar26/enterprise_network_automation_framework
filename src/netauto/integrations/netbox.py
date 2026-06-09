from ..config.settings import Env_Setting
import pynetbox
from ..utils import logger
from rich import print as r_print

log = logger.get_logger("NetBoxClient_Logger")

class NetBoxClient:
    """A thin wrapper around NetBox API calls for device and interface lookup."""

    def __init__(self, Netbox_url: str, Netbox_token: str):
        """Initialize the NetBox client with API URL and token."""
        log.info("NetBoxClient initialized")
        self.Netbox_url = Netbox_url
        self.Netbox_token = Netbox_token
        self.nb = pynetbox.Api(url=self.Netbox_url, token=self.Netbox_token)

    def get_device_by_name(self, device_name):
        """Return the NetBox device record for the given device name."""
        log.info(
            f"Connecting to NetBox @{self.Netbox_url} to get details for device '{device_name}'..."
        )
        try:
            device = self.nb.dcim.devices.get(name=device_name)
            if device:
                log.info(f"Device '{device_name}' found in NetBox.")
                return device
            log.warning(f"Device '{device_name}' not found in NetBox.")
            return None
        except ValueError as exc:
            log.error(
                f"Invalid NetBox configuration or request for device '{device_name}': {exc}"
            )
        except AttributeError as exc:
            log.error(
                f"Unexpected NetBox response structure while fetching device '{device_name}': {exc}"
            )
        except Exception as exc:
            log.error(
                f"An error occurred while fetching device '{device_name}' from NetBox: {exc}"
            )
        return None

    def get_interfaces(self, device_name) -> list:
        """Return interface details for the named device if it exists in NetBox."""
        log.info(
            f"Connecting to NetBox @{self.Netbox_url} to get interface details for device '{device_name}'..."
        )
        try:
            device = self.nb.dcim.devices.get(name=device_name)
            if not device:
                log.error(f"Device '{device_name}' does not exist in NetBox.")
                return None

            log.info(f"Device '{device_name}' exists in NetBox. Fetching interface details...")
            interfaces = self.nb.dcim.interfaces.filter(device=device_name)
            interface_details = []
            if interfaces:
                for i in interfaces:
                    interface_details.append(dict(i))
                # return interface_details
                log.info(f"Collected interface details for device '{device_name}'.")
                return interface_details

            log.warning(
                f"No interface records were returned for device '{device_name}' in NetBox."
            )
            return None
        except ValueError as exc:
            log.error(
                f"Invalid NetBox configuration or request while fetching interfaces for '{device_name}': {exc}"
            )
        except AttributeError as exc:
            log.error(
                f"Unexpected NetBox response structure while fetching interfaces for '{device_name}': {exc}"
            )
        except Exception as exc:
            log.error(
                f"An error occurred while fetching interfaces for '{device_name}' from NetBox: {exc}"
            )
        return None


if __name__ == "__main__":
    Setting = Env_Setting()
    netbox = NetBoxClient(
        Netbox_url=Setting.NETBOX_PROD_URL,
        Netbox_token=Setting.NETBOX_PROD_TOKEN_RW.get_secret_value(),
    )
    output = netbox.get_device_by_name(device_name="IN-HYD-LAB1-ACC-01")
    print(output)
    
    # output = netbox.get_interfaces(device_name="IN-HYD-LAB1-ACC-01")
    # r_print(output)